import copy
import datetime as dt
import decimal
import uuid
from collections import defaultdict
from contextlib import suppress

from csp.decorators import csp_replace
from django.contrib import messages
from django.db.models import Count, Q
from django.db.models.functions import TruncYear
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.utils.functional import cached_property
from django.utils.timezone import now
from django.utils.translation import override
from django.views.generic import (
    DeleteView,
    DetailView,
    FormView,
    ListView,
    TemplateView,
)
from django_context_decorator import context
from django_scopes import scopes_disabled
from pretalx.common.mail import mail_send_task
from pretalx.common.models import ActivityLog
from pretalx.common.views import CreateOrUpdateView
from pretalx.common.views.mixins import PermissionRequired, Sortable
from pretalx.event.models import Event

from pretalx_com.forms import (
    BlogForm,
    CustomerFilterForm,
    EventComInvoiceForm,
    EventComProfileForm,
    MaintenanceAnnouncementForm,
    MinimalBillingForm,
)
from pretalx_com.models import (
    BlogPost,
    EventComInvoice,
    PretalxInstance,
    PretalxInstanceEvent,
    get_event_com_profile,
)
from pretalx_com.prices import PRICES
from pretalx_com.utils import get_monthly_report_data, get_weekly_report_data


class AdminPermissionRequired(PermissionRequired):
    permission_required = "com.administer"


class OrgaBlogList(AdminPermissionRequired, ListView):
    template_name = "pretalx_com/orga_blog_list.html"
    model = BlogPost
    context_object_name = "posts"


class OrgaBlogView(AdminPermissionRequired, CreateOrUpdateView):
    template_name = "pretalx_com/orga_blog.html"
    model = BlogPost
    context_object_name = "post"
    form_class = BlogForm

    def get_object(self):
        with suppress(self.model.DoesNotExist, AttributeError):
            return super().get_object()

    def get_success_url(self):
        return "/orga/p/blog/"

    def form_valid(self, form, *args, **kwargs):
        form.save()
        return super().form_valid(form, *args, **kwargs)


@method_decorator(csp_replace(IMG_SRC="'self' https://quickchart.io"), name="dispatch")
class Business(AdminPermissionRequired, TemplateView):
    template_name = "pretalx_com/business.html"

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        with scopes_disabled():
            invoices = defaultdict(list)
            for invoice in EventComInvoice.objects.all():
                invoices[invoice.date.year].append(invoice)
        result["years"] = {
            year: {
                "count": len(invoices[year]),
                "sum": sum(
                    invoice.amount for invoice in invoices[year] if invoice.paid
                ),
                "sum_with_unpaid": int(
                    sum(invoice.amount for invoice in invoices[year])
                ),
                "invoices": invoices[year],
            }
            for year in sorted(invoices.keys(), reverse=True)
        }
        return result


class CustomerList(AdminPermissionRequired, Sortable, ListView):
    model = Event
    template_name = "pretalx_com/customer_list.html"
    context_object_name = "events"
    default_sort_field = "-pk"
    sortable_fields = ["pk", "name", "date_from", "is_public", "last_activity"]
    paginate_by = 50

    @context
    @cached_property
    def filter_form(self):
        return CustomerFilterForm(data=self.request.GET)

    def get_queryset(self):
        with scopes_disabled():
            for event in Event.objects.filter(com__isnull=True):
                get_event_com_profile(event)
            qs = (
                Event.objects.all()
                .select_related("com", "organiser")
                .prefetch_related("com_invoices")
            )
            if self.filter_form.is_valid():
                qs = self.filter_form.filter_queryset(qs)
            return self.sort_queryset(qs)


class CustomerDetail(AdminPermissionRequired, FormView):
    template_name = "pretalx_com/customer_detail.html"
    form_class = EventComProfileForm

    def get_success_url(self):
        return f"/orga/p/customers/{self.request.event.slug}/"

    def form_valid(self, form, *args, **kwargs):
        form.save()
        return super().form_valid(form, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = get_event_com_profile(self.request.event)
        return kwargs


class InvoiceDetail(AdminPermissionRequired, CreateOrUpdateView):
    model = EventComInvoice
    form_class = EventComInvoiceForm
    template_name = "pretalx_com/invoice_detail.html"

    def get_object(self):
        with suppress(self.model.DoesNotExist, AttributeError):
            return super().get_object()

    def get_success_url(self):
        return f"/orga/p/customers/{self.request.event.slug}/"

    def form_valid(self, form, *args, **kwargs):
        form.instance.event = self.request.event
        form.save()
        return super().form_valid(form, *args, **kwargs)


class DeleteInvoice(AdminPermissionRequired, DeleteView):
    model = EventComInvoice
    template_name = "pretalx_com/invoice_delete.html"

    def get_success_url(self):
        return f"/orga/p/customers/{self.request.event.slug}/"


class OrgaInstanceList(AdminPermissionRequired, Sortable, ListView):
    template_name = "pretalx_com/instance_list.html"
    model = PretalxInstance
    context_object_name = "instances"
    default_sort_field = "-last_check"
    sortable_fields = ["name", "last_check", "error_count"]

    def get_queryset(self):
        queryset = self.sort_queryset(super().get_queryset())
        _filter = self.request.GET.get("show")
        if _filter == "unknown":
            queryset = queryset.filter(
                Q(name__isnull=True) | Q(name__exact="") | Q(name__startswith="??")
            )
        search = self.request.GET.get("q")
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search)
                | Q(id__icontains=search)
                | Q(events__name__icontains=search)
            )
        queryset = queryset.annotate(event_count=Count("events", distinct=True))
        return queryset

    def post(self, request, *args, **kwargs):
        with suppress(Exception):
            if request.POST.get("action") == "delete":
                instance = PretalxInstance.objects.get(pk=request.POST.get("instance"))
                instance.delete()
                messages.success(request, "Instance deleted")
            elif request.POST.get("action") == "name":
                instance = PretalxInstance.objects.get(pk=request.POST.get("instance"))
                name = request.POST.get("name")
                if name.startswith("MERGE "):
                    other_instance = PretalxInstance.objects.filter(
                        name=name[6:].strip()
                    ).first()
                    if other_instance:
                        instance.merge_with(other_instance)
                        messages.success(request, "Instance merged")
                    else:
                        messages.error(request, "Instance not found")
                else:
                    instance.name = name
                    instance.save()
                    messages.success(request, "Instance name saved")
            elif request.POST.get("action") == "create":
                name = request.POST.get("name")
                if name:
                    name = name.lower().strip()
                    if PretalxInstance.objects.filter(name__iexact=name).count():
                        messages.error(request, "Instance exists already")
                    else:
                        PretalxInstance.objects.create(
                            name=name,
                            id=uuid.uuid4().hex,
                            last_check=now() - dt.timedelta(days=1),
                        )
                        messages.success(request, "Instance created")
        return self.get(request, *args, **kwargs)


class OrgaInstanceDetail(AdminPermissionRequired, DetailView):
    template_name = "pretalx_com/instance_detail.html"
    model = PretalxInstance
    context_object_name = "instance"


@method_decorator(csp_replace(IMG_SRC="'self' https://quickchart.io"), name="dispatch")
class OrgaInstanceStats(AdminPermissionRequired, TemplateView):
    template_name = "pretalx_com/instance_stats.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        instances = (
            PretalxInstance.objects.annotate(event_count=Count("events", distinct=True))
            .filter(event_count__gt=0)
            .prefetch_related("events")
        )
        pretalx_com = instances.get(name="pretalx.com")
        instances = instances.exclude(pk=pretalx_com.pk)

        ctx["instance_count"] = instances.count()
        ctx["instance_event_count"] = (
            PretalxInstanceEvent.objects.exclude(instance=pretalx_com)
            .filter(ignored=False)
            .count()
        )
        ctx["com_event_count"] = pretalx_com.events.all().count()
        ctx["event_count"] = ctx["instance_event_count"] + ctx["com_event_count"]
        ctx["com_percent"] = (
            round(
                ctx["com_event_count"]
                / (ctx["instance_event_count"] + ctx["com_event_count"])
                * 100,
                2,
            )
            if ctx["com_event_count"]
            else 0
        )

        base_qs = PretalxInstanceEvent.objects.filter(ignored=False)

        instance_year_counts = (
            base_qs.exclude(instance=pretalx_com)
            .annotate(year=TruncYear("date_from"))
            .values("year")
            .annotate(count=Count("year"))
        )
        total_year_counts = (
            base_qs.annotate(year=TruncYear("date_from"))
            .values("year")
            .annotate(count=Count("year"))
        )
        com_year_counts = (
            base_qs.filter(instance=pretalx_com)
            .annotate(year=TruncYear("date_from"))
            .values("year")
            .annotate(count=Count("year"))
        )
        years = sorted(set([i["year"].year for i in total_year_counts]))

        instance_year_counts = {
            i["year"].year: i["count"] for i in instance_year_counts
        }
        total_year_counts = {i["year"].year: i["count"] for i in total_year_counts}
        com_year_counts = {i["year"].year: i["count"] for i in com_year_counts}

        ctx["years_stats"] = [
            {
                "year": year,
                "count": total_year_counts.get(year, 0),
                "com_count": com_year_counts.get(year, 0),
                "instance_count": instance_year_counts.get(year, 0),
                "com_percent": (
                    com_year_counts.get(year, 0) / total_year_counts.get(year, 0) * 100
                    if total_year_counts.get(year, 0)
                    else 0
                ),
            }
            for year in years
        ]

        return ctx


@method_decorator(csp_replace(IMG_SRC="'self' https://quickchart.io"), name="dispatch")
class OrgaInstanceEvents(AdminPermissionRequired, TemplateView):
    template_name = "pretalx_com/instance_events.html"

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)

        qs = PretalxInstanceEvent.objects.filter(ignored=False)
        if self.request.GET.get("show") == "com":
            qs = qs.filter(instance__name="pretalx.com")
        elif self.request.GET.get("show") == "selfhosted":
            qs = qs.exclude(instance__name="pretalx.com")
        total_year_counts = (
            qs.annotate(year=TruncYear("date_from"))
            .values("year")
            .annotate(count=Count("year"))
        )
        years = sorted(set([i["year"].year for i in total_year_counts]))

        sections = []
        for year in years:
            sections.append(
                {
                    "year": year,
                    "events": qs.filter(date_from__year=year, ignored=False).order_by(
                        "name"
                    ),
                }
            )

        ctx["sections"] = list(reversed(sections))
        return ctx

    def post(self, request, *args, **kwargs):
        if request.POST.get("ignore"):
            event = PretalxInstanceEvent.objects.get(pk=request.POST.get("ignore"))
            event.ignored = True
            event.save()
        return self.get(request, *args, **kwargs)


class OrgaCalendar(AdminPermissionRequired, TemplateView):
    template_name = "pretalx_com/calendar.html"

    @scopes_disabled()
    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        events = Event.objects.filter(
            Q(com__unlock_activation=True)
            | Q(com_invoices__date__isnull=False)
            | Q(is_public=True),
            # date_from__gte=now().date(),
        )
        dates = []
        for event in events:
            if event.cfp.deadline:  # and event.cfp.deadline > now():
                dates.append(
                    {
                        "url": event.orga_urls.base,
                        "event": str(event.name),
                        "title": f"Deadline: {event.name}",
                        "timestamp": event.cfp.deadline,
                        "start": event.cfp.deadline.date().isoformat(),
                        "table_title": "CfP deadline",
                        "color": "grey",
                    }
                )
            for submission_type in event.submission_types.filter(
                deadline__isnull=False
            ):  # deadline__gte=now()):
                dates.append(
                    {
                        "url": event.orga_urls.base,
                        "event": str(event.name),
                        "title": f"Deadline: {submission_type.name} ({event.name})",
                        "timestamp": submission_type.deadline,
                        "start": submission_type.deadline.date().isoformat(),
                        "table_title": "Submission type deadline",
                        "color": "grey",
                    }
                )
            dates.append(
                {
                    "url": event.orga_urls.base,
                    "event": str(event.name),
                    "title": str(event.name),
                    "timestamp": event.datetime_from,
                    "table_title": f"{event.name} running",
                    "start": event.date_from.isoformat(),
                    "end": event.date_to.isoformat(),
                    "color": "#" + (event.get_primary_color().strip("#")),
                }
            )

            # from dateutil import rrule
            # date_range = rrule.rrule(
            #     rrule.DAILY,
            #     count=(event.date_to - event.date_from).days + 1,
            #     dtstart=event.datetime_from,
            # )
            # for day in date_range:
            #     dates.append(
            #         {"event": event, "timestamp": day, "title": "Event running"}
            #     )
        # print(dates)
        dates.sort(key=lambda entry: (entry["timestamp"], entry["url"]))
        result["calendar"] = dates
        return result


class MaintenanceAnnouncement(AdminPermissionRequired, FormView):
    template_name = "pretalx_com/maintenance.html"
    form_class = MaintenanceAnnouncementForm

    def form_valid(self, form):
        date = form.cleaned_data["date"]
        text = form.cleaned_data["email_text"]
        subject = f"Maintenance: pretalx.com, {date.date()}"
        today = now().date()
        eight_months_ago = today - dt.timedelta(days=240)
        with scopes_disabled():
            future_emails = Event.objects.filter(date_from__gte=today).values_list(
                "email", flat=True
            )
            invoiced_emails = EventComInvoice.objects.filter(
                date__gte=eight_months_ago
            ).values_list("event__email", flat=True)
        emails = set(future_emails) | set(invoiced_emails) | {"r@rixx.de"}

        for email in emails:
            languages = Event.objects.filter(email=email).values_list(
                "locale", flat=True
            )
            language = "de" if "de" in languages else "en"
            with override(language):
                mail_send_task.apply_async(
                    kwargs={
                        "to": [email],
                        "subject": subject,
                        "body": str(text),
                        "html": None,
                        "reply_to": "support@pretalx.com",
                        "event": None,
                    },
                    ignore_result=True,
                )
        messages.success(
            self.request,
            f"Sent maintenance announcement to {len(emails)} event organisers.",
        )
        return redirect("/orga/p/maintenance/")

    def form_invalid(self, form):
        return redirect("/orga/p/maintenance/")


@method_decorator(scopes_disabled(), name="dispatch")
class Reporting(AdminPermissionRequired, TemplateView):
    template_name = "pretalx_com/reporting.html"

    @context
    @cached_property
    def today(self):
        return now().date()

    @context
    @cached_property
    def last_activities(self):
        return ActivityLog.objects.filter(
            Q(action_type__startswith="pretalx.com")
            | Q(action_type="pretalx.event.delete")
            | Q(action_type="pretalx.organiser.delete")
        )[:25]

    @context
    @cached_property
    def weekly_report(self):
        return get_weekly_report_data()

    @context
    @cached_property
    def monthly_report(self):
        return get_monthly_report_data()


class BulkBillingCalculator(AdminPermissionRequired, TemplateView):
    template_name = "pretalx_com/bulk_billing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prices"] = copy.deepcopy(PRICES)
        discount = 1
        context["prices"]["price_steps"] = [
            [round(decimal.Decimal(str(element)) * discount, 2) for element in step]
            for step in context["prices"]["price_steps"]
        ]
        context["discounts"] = {
            5: 10,
            10: 15,
        }
        context["form"] = MinimalBillingForm(select_widget=True)
        return context
