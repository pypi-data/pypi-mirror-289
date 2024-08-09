import copy
import decimal
from contextlib import suppress

from django.contrib import messages
from django.contrib.staticfiles.storage import staticfiles_storage
from django.db import transaction
from django.http import HttpResponse
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView
from pretalx.common.views.mixins import PermissionRequired

from pretalx_com.forms import BillingForm, PrivacyForm
from pretalx_com.models import (
    DJCRMOrganiser,
    EventComInvoice,
    OrganiserComProfile,
    get_event_com_profile,
)
from pretalx_com.prices import PRICES


class BillingView(PermissionRequired, FormView):
    template_name = "pretalx_com/billing.html"
    permission_required = "com.view_billing"
    form_class = BillingForm

    def get_permission_object(self):
        return self.request.event

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prices"] = copy.deepcopy(PRICES)
        com = get_event_com_profile(self.request.event)
        if com.agreed_price:
            context["agreed_vat"] = com.agreed_price * decimal.Decimal("0.19")
        elif com.discount and com.discount > 0:
            context["discount_percent"] = int(com.discount * 100)
        discount = 1 - (com.discount or decimal.Decimal("0"))
        context["prices"]["price_steps"] = [
            [round(decimal.Decimal(str(element)) * discount, 2) for element in step]
            for step in context["prices"]["price_steps"]
        ]
        o_com = getattr(
            self.request.event.organiser, "com", None
        ) or OrganiserComProfile.objects.create(organiser=self.request.event.organiser)
        context["o_com"] = o_com
        context["com"] = com
        return context

    def post(self, request, *args, **kwargs):
        # Don't create a second invoice
        if self.request.event.com_invoices.all().exists():
            return self.get(request, *args, **kwargs)
        return super().post(request, *args, **kwargs)

    def get_form_kwargs(self, *args, **kwargs):
        form_kwargs = super().get_form_kwargs(*args, **kwargs)
        form_kwargs["instance"] = getattr(self.request.event.organiser, "djcrm", None)
        form_kwargs["event"] = self.request.event
        return form_kwargs

    @transaction.atomic
    def form_valid(self, form):
        form.instance.organiser = self.request.event.organiser
        try:
            form.instance.sync()
        except Exception:
            messages.error(
                self.request,
                _(
                    "Unable to create an invoice at this time – please get in touch with us at sales@pretalx.com"
                ),
            )
            return self.form_invalid(form)
        discount = None
        ticket_price_level = None
        attendee_level = None
        com = get_event_com_profile(self.request.event)
        if com.agreed_price:
            price = com.agreed_price
        else:
            ticket_price_level = form.cleaned_data["tickets"]
            attendee_level = form.cleaned_data["attendees"]
            price = PRICES["price_steps"][ticket_price_level][attendee_level]
            if discount := com.discount:
                price = decimal.Decimal(str(price)) * (1 - discount)
                price = float(str(round(price, 2)))
        european_countries = [
            "AT",
            "BE",
            "BG",
            "HR",
            "CY",
            "CZ",
            "DK",
            "EE",
            "FI",
            "FR",
            "DE",
            "GR",
            "HU",
            "IE",
            "IT",
            "LV",
            "LT",
            "LU",
            "MT",
            "NL",
            "PL",
            "PT",
            "RO",
            "SK",
            "SI",
            "ES",
            "SE",
        ]
        is_german = form.instance.address_country.name == "Germany"
        with_vat = is_german or (
            form.instance.address_country.code in european_countries
            and not form.cleaned_data["reverse_charge"]
        )
        try:
            EventComInvoice.create_from_data(
                price=price,
                customer=form.instance.nr,
                tax_rate="19.00" if with_vat else "0.00",
                reverse_charge=(
                    form.cleaned_data["reverse_charge"] if not is_german else None
                ),
                event=self.request.event,
                discount=discount if (discount and discount > 0) else None,
                ticket_price_level=ticket_price_level,
                attendee_level=attendee_level,
                user=self.request.user,
            )
        except Exception:  # noqa
            messages.error(
                self.request,
                _(
                    "Unable to create an invoice at this time – please get in touch with us at sales@pretalx.com"
                ),
            )
            return self.form_invalid(form)
        messages.success(
            self.request,
            _(
                "Thank you for choosing pretalx! You can download your invoice below, and you can immediatly take your event live via your event dashboard. "
                "And remember: You can contact us via support@pretalx.com if there is anything we can help you with."
            ),
        )
        return self.get(self.request)


class OrgaPrivacyView(PermissionRequired, FormView):
    template_name = "pretalx_com/privacy_organiser.html"
    permission_required = "com.view_privacy"
    form_class = PrivacyForm

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self.request.organiser, "djcrm"):
            with suppress(Exception):
                DJCRMOrganiser.objects.create(organiser=self.request.organiser)
        return super().dispatch(request, *args, **kwargs)

    def get_permission_object(self):
        return self.request.organiser

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.request.organiser.djcrm
        return kwargs

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path

    def post(self, request, *args, **kwargs):
        if self.request.POST.get("action", "") != "file":
            return super().post(request, *args, **kwargs)
        language = self.request.POST.get("language", "en")
        if language not in ("en", "de"):
            language = "en"
        filename = (
            f"pretalx_com/terms/auftragsdatenverarbeitung-template-{language}.pdf"
        )
        with staticfiles_storage.open(filename) as f:
            content = f.read()
        # org = self.request.organiser.djcrm
        # address_parts = [org.address_street, org.address_city, org.address_country.name]
        # address_line = ", ".join(a for a in address_parts if a)
        # today = now().strftime("%Y-%m-%d")
        # data = {
        #     'pretalx_customer_line_1': str(self.request.organiser.name),
        #     'pretalx_customer_line_2': address_line,
        #     'pretalx_date': f'Kornwestheim, {today}',
        #     'pretalx_slug': self.request.organiser.slug,
        # }
        response = HttpResponse(
            content,
            headers={
                "Content-Type": "application/pdf",
                "Content-Disposition": f'attachment; filename="pretalx_data_{self.request.organiser.slug}.pdf"',
            },
        )
        return response
