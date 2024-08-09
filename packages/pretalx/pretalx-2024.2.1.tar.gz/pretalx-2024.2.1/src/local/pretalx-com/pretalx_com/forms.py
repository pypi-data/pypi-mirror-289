from django import forms
from django.db import transaction
from django.db.models import OuterRef, Subquery
from django.forms import ValidationError
from django.utils import timezone, translation
from django.utils.translation import gettext_lazy as _
from i18nfield.fields import I18nFormField, I18nTextarea
from pretalx.common.forms.fields import PasswordConfirmationField, PasswordField
from pretalx.common.models import ActivityLog
from pretalx.common.text.phrases import phrases
from pretalx.event.models import Organiser, Team
from pretalx.person.models import User

from pretalx_com.models import (
    BlogPost,
    DJCRMOrganiser,
    EventComInvoice,
    EventComProfile,
    OrganiserComProfile,
    get_event_com_profile,
)
from pretalx_com.prices import PRICES
from pretalx_com.utils import get_deletion_candidates


class RegistrationForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        label=_("What's your name?"),
        help_text=_(
            "Please choose your name, not your company's name. You will be able to give access to your team later."
        ),
    )
    email = forms.EmailField(
        label=_("And your email address?"),
        help_text=_(
            "We'll only ever use this address to send you notifications about your events, and in emergencies. No spam, no advertising, promise."
        ),
    )
    password = PasswordField(label=_("Password"), required=False)
    password_repeat = PasswordConfirmationField(
        label=_("Password (again, to make sure)"),
        required=False,
        confirm_with="register_password",
    )
    organiser_name = forms.CharField(
        max_length=200,
        label=_("Who is running your event?"),
        help_text=_("Name of your company/association/institution."),
    )
    organiser_slug = forms.CharField(
        max_length=40,
        label=_("Short form"),
        help_text=_("A short form of your organiser's name, to be used in URLs."),
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if self.user:
            self.fields.pop("name")
            self.fields.pop("email")
        else:
            self.fields["name"].widget.attrs["placeholder"] = _("Jane Doe")
            self.fields["email"].widget.attrs["placeholder"] = _("jdoe@corp.org")
        self.fields["password"].widget.attrs["placeholder"] = "***"
        self.fields["password_repeat"].widget.attrs["placeholder"] = "***"
        self.fields["organiser_name"].widget.attrs["placeholder"] = _(
            "Networking Association ltd"
        )
        self.fields["organiser_slug"].widget.attrs["placeholder"] = _("netorg")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email__iexact=email).exists():
            raise ValidationError(
                _(
                    "We already have a user with that email address. Did you already register "
                    "before and just need to log in?"
                )
            )
        return email.lower()

    def clean_organiser_slug(self):
        slug = self.cleaned_data.get("organiser_slug")
        if Organiser.objects.filter(slug__iexact=slug).exists():
            raise ValidationError(
                _(
                    "We already have an organiser with this short form. Did you already register "
                    "before and just need to log in?"
                )
            )
        return slug.lower()

    def clean(self):
        data = super().clean()
        if data.get("password") != data.get("password_repeat"):
            self.add_error(
                "password_repeat", ValidationError(phrases.base.passwords_differ)
            )

    @transaction.atomic
    def save(self):
        data = self.cleaned_data
        user = self.user or User.objects.create_user(
            name=data.get("name"),
            email=data.get("email"),
            password=data.get("password"),
            locale=translation.get_language(),
            timezone=timezone.get_current_timezone_name(),
        )
        organiser = Organiser.objects.create(
            name=data.get("organiser_name"), slug=data.get("organiser_slug")
        )
        team = Team.objects.create(
            organiser=organiser,
            name=str(organiser.name) + " Team",
            all_events=True,
            can_create_events=True,
            can_change_teams=True,
            can_change_organiser_settings=True,
            can_change_event_settings=True,
            can_change_submissions=True,
            is_reviewer=True,
        )
        team.members.add(user)
        return user


class EventComProfileForm(forms.ModelForm):
    activations_left = forms.IntegerField(
        required=False,
        label=_("Activations left"),
        help_text=_("Organiser level setting!"),
    )
    activations_reset_date = forms.DateField(
        required=False,
        label=_("Activations reset date"),
        help_text=_(
            "Organiser level setting! Activations will be set to 0 on this date."
        ),
    )
    organiser_discount = forms.DecimalField(
        required=False,
        label=_("Organiser discount"),
        help_text=_(
            "Percentage discount for this organiser, to be used at all future events."
        ),
    )

    def __init__(self, *args, **kwargs):
        instance = kwargs.get("instance")
        initial = kwargs.get("initial", {})
        if instance:
            com = getattr(instance.event.organiser, "com", None)
            if com:
                initial["activations_left"] = com.activations_left
                initial["activations_reset_date"] = com.activations_reset_date
                initial["organiser_discount"] = com.discount
            else:
                OrganiserComProfile.objects.create(organiser=instance.event.organiser)
        kwargs["initial"] = initial
        super().__init__(*args, **kwargs)

    def save(self):
        result = super().save()
        data = self.cleaned_data
        com = self.instance.event.organiser.com
        com.activations_left = data.get("activations_left")
        com.activations_reset_date = data.get("activations_reset_date")
        com.discount = data.get("organiser_discount")
        com.save()
        return result

    class Meta:
        model = EventComProfile
        fields = (
            "unlock_activation",
            "agreed_price",
            "organiser_discount",
            "discount",
            "activations_left",
            "activations_reset_date",
            "skip_deletion",
            "warned_about_deletion",
        )


class EventComInvoiceForm(forms.ModelForm):
    class Meta:
        model = EventComInvoice
        fields = ("amount", "number", "date", "paid", "ignore_paid", "invoice")


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = "__all__"


class MinimalBillingForm(forms.Form):
    attendees = forms.IntegerField(
        min_value=0, max_value=len(PRICES["attendee_steps"]), required=False
    )
    tickets = forms.IntegerField(
        min_value=0, max_value=len(PRICES["ticket_steps"]), required=False
    )

    def __init__(self, *args, event=None, select_widget=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.event = event
        if event:
            com = get_event_com_profile(event)
            if com.agreed_price:
                self.fields["attendees"].required = False
                self.fields["tickets"].required = False
        if select_widget:
            self.fields["attendees"] = forms.ChoiceField(
                choices=[(i, step) for i, step in enumerate(PRICES["attendee_steps"])]
            )
            self.fields["tickets"] = forms.ChoiceField(
                choices=[(i, step) for i, step in enumerate(PRICES["ticket_steps"])]
            )


class BillingForm(MinimalBillingForm, forms.ModelForm):
    read_terms = forms.BooleanField(
        label=_("I have read and accepted the Terms of Service"),
        help_text=_(
            'Please read <a href="{url}" target="_blank">the Terms of Service, and the privacy policy.'
        ).format(url="https://pretalx.com/p/terms"),
        required=True,
    )
    reverse_charge = forms.CharField(
        label=_("VAT ID (EU Countries)"),
        help_text=_(
            "If you are from a country in the EU except for Germany, please provide your VAT ID for reverse charge rules to apply."
        ),
        required=False,
    )

    def __init__(self, *args, event=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["address_country"].help_text = _(
            "If you are located in Germany, an additional 19% VAT will apply!"
        )
        for field in (
            "address_company",
            "address_street",
            "address_zipcode",
            "address_city",
        ):
            self.fields[field].required = True

    class Meta:
        model = DJCRMOrganiser
        fields = (
            "address_name",
            "address_company",
            "address_supplement",
            "address_street",
            "address_zipcode",
            "address_city",
            "address_country",
            "language",
            "reverse_charge",
            "read_terms",
            "attendees",
            "tickets",
        )


class SupportForm(forms.Form):
    message = forms.CharField(
        label=_("How can we help you?"),
        help_text=_(
            "Please describe your problem as detailed as possible. Where did it occur? What did you want to do, what happened instead?"
        ),
        required=True,
        widget=forms.Textarea,
    )
    contact_method = forms.ChoiceField(
        label=_("How should we contact you?"),
        help_text=_(
            "We will try to comply with your choice, but in case we cannot phone you right now, we will fall back to emails."
        ),
        choices=(("mail", _("E-mail")), ("phone", _("Phone"))),
        required=False,
        widget=forms.RadioSelect,
    )
    email = forms.EmailField(label=_("Contact email address"), required=True)
    phone = forms.CharField(label=_("Contact phone number"), required=False)
    time = forms.CharField(
        label=_("When would you like us to call?"),
        help_text=_("E.g. now, tomorrow, in the afternoon …"),
        required=False,
    )


class ContactForm(forms.Form):
    message = forms.CharField(
        label=_("How can we help you?"),
        help_text=_(
            "Please describe your problem as detailed as possible. Where did it occur? What did you want to do, what happened instead?"
        ),
        required=True,
        widget=forms.Textarea,
    )
    event = forms.CharField(
        label=_("Event"),
        required=False,
    )
    email = forms.EmailField(label=_("Contact email address"), required=True)


class PrivacyForm(forms.ModelForm):
    class Meta:
        model = DJCRMOrganiser
        fields = ("dsgvo_document",)


class MaintenanceAnnouncementForm(forms.Form):
    date = forms.DateTimeField(help_text=_("Time of maintenance start in UTC"))
    email_text = I18nFormField(
        label=_("Email text"),
        help_text=_("The subject will be set to 'Maintenance: pretalx.com, < date >'."),
        widget=I18nTextarea,
        initial={"de": "Hallo", "en": "Hi"},
        locales=["de", "en"],
    )

    class Meta:
        widgets = {
            "date": forms.DateInput(attrs={"class": "datetimepickerfield"}),
            "email_text": I18nTextarea,
        }


class CustomerFilterForm(forms.Form):
    deletion_candidate = forms.ChoiceField(
        label=_("Deletion candidate"),
        help_text="In the past, not invoiced, not unlocked or public, last activity more than 2 months ago.",
        choices=(
            ("all", "All"),
            ("yes", _("Only deletion candidates")),
            ("no", _("No deletion candidates")),
        ),
        required=False,
    )
    is_public = forms.ChoiceField(
        label=_("Public"),
        choices=(
            ("all", "All"),
            ("yes", _("only public")),
            ("no", _("only nonpublic")),
        ),
        required=False,
    )
    invoiced = forms.ChoiceField(
        label=_("Invoiced"),
        choices=(
            ("all", "All"),
            ("yes", _("only invoiced")),
            ("no", _("only non-invoiced")),
        ),
        required=False,
    )
    paid = forms.ChoiceField(
        label=_("Paid"),
        choices=(("all", "All"), ("yes", _("only paid")), ("no", _("only unpaid"))),
        required=False,
    )
    ignore_paid = forms.ChoiceField(
        label=_("Ignore paid"),
        choices=(
            ("all", "All"),
            ("yes", _("only ignore-paid")),
            ("no", _("only non-ignore-paid")),
        ),
        required=False,
    )
    cfp_open = forms.ChoiceField(
        label=_("CFP open"),
        choices=(("all", "All"), ("yes", _("CfP open")), ("no", _("CfP closed"))),
        required=False,
    )

    def filter_queryset(self, qs):
        if self.cleaned_data.get("delete_candidate") == "yes":
            qs = get_deletion_candidates(qs, mode="filter")
        elif self.cleaned_data.get("delete_candidate") == "no":
            qs = get_deletion_candidates(qs, mode="exclude")
        else:
            last_activities = (
                ActivityLog.objects.filter(event_id=OuterRef("pk"))
                .order_by("-id")
                .values("timestamp")[:1]
            )
            qs = qs.annotate(last_activity=Subquery(last_activities))
        joined = (
            ActivityLog.objects.filter(event_id=OuterRef("pk"))
            .order_by("id")
            .values("timestamp")[:1]
        )
        qs = qs.annotate(joined=Subquery(joined))
        _now = timezone.now()
        if self.cleaned_data.get("is_public") == "yes":
            qs = qs.filter(is_public=True)
        elif self.cleaned_data.get("is_public") == "no":
            qs = qs.filter(is_public=False)
        if self.cleaned_data.get("invoiced") == "yes":
            qs = qs.filter(com_invoices__isnull=False)
        elif self.cleaned_data.get("invoiced") == "no":
            qs = qs.filter(com_invoices__isnull=True)
        if self.cleaned_data.get("paid") == "yes":
            qs = qs.filter(com_invoices__paid=True)
        elif self.cleaned_data.get("paid") == "no":
            qs = qs.filter(com_invoices__paid=False)
        if self.cleaned_data.get("ignore_paid") == "yes":
            qs = qs.filter(com_invoices__ignore_paid=True)
        elif self.cleaned_data.get("ignore_paid") == "no":
            qs = qs.filter(com_invoices__ignore_paid=False)
        if self.cleaned_data.get("cfp_open") == "yes":
            qs = qs.filter(cfp__deadline__gte=_now)
        elif self.cleaned_data.get("cfp_open") == "no":
            qs = qs.filter(cfp__deadline__lt=_now)
        return qs
