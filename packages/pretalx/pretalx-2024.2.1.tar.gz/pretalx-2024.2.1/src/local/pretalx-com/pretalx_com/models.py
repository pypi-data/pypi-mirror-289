import datetime as dt
import json
import string

import requests
from django.conf import settings
from django.core.files.base import ContentFile
from django.db import models, transaction
from django.utils.crypto import get_random_string
from django.utils.functional import cached_property
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django_scopes import scope
from i18nfield.strings import LazyI18nString
from pretalx.common.mail import mail_send_task
from pretalx.common.models.log import ActivityLog
from pretalx.common.models.mixins import LogMixin
from pretalx.common.text.path import path_with_hash
from pretalx.event.models import Event, Organiser

from .versions import get_new_features


def generate_secret():
    return get_random_string(
        allowed_chars=string.ascii_lowercase + string.digits, length=32
    )


def invoice_path(instance, filename):
    if not instance.secret:
        instance.secret = generate_secret()
    return f"{instance.event.slug}/invoice/{instance.secret}/{path_with_hash(filename)}"


def dsgvo_path(instance, filename):
    return f"{instance.organiser.slug}/{path_with_hash(filename)}"


def get_event_com_profile(event):
    with scope(event=event):
        if hasattr(event, "com"):
            com = event.com
        else:
            com = EventComProfile.objects.create(event=event)
            if organiser_com := getattr(event.organiser, "com", None):
                com.discount = organiser_com.discount
                com.save()
    return com


class DJCRMOrganiser(LogMixin, models.Model):
    organiser = models.OneToOneField(
        to=Organiser, on_delete=models.CASCADE, related_name="djcrm"
    )
    nr = models.CharField(max_length=100, db_index=True, unique=True, blank=True)
    name = models.CharField(max_length=190)
    address_name = models.CharField(
        verbose_name=_("Person name"), default="", max_length=190, blank=True
    )
    address_company = models.CharField(
        verbose_name=_("Company name"), default="", max_length=190, blank=True
    )
    address_supplement = models.CharField(
        verbose_name=_("Address supplement"), default="", max_length=190, blank=True
    )
    address_street = models.CharField(
        verbose_name=_("Street and number"), default="", max_length=190, blank=True
    )
    address_zipcode = models.CharField(
        verbose_name=_("ZIP code"), default="", max_length=190, blank=True
    )
    address_city = models.CharField(
        verbose_name=_("City"), default="", max_length=190, blank=True
    )
    address_country = CountryField(verbose_name=_("Country"), default="DE")

    language = models.CharField(
        verbose_name=_("Language"),
        help_text=_("In which language do you want your invoice to be?"),
        max_length=50,
        choices=(("de", "German"), ("en", "English")),
        default="de",
    )

    dsgvo_document = models.FileField(
        null=True, blank=True, upload_to=dsgvo_path, max_length=240
    )

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"DJCRM #{self.nr} for {self.organiser.name}"

    @property
    def as_dict(self):
        data = {
            attr: getattr(self, attr)
            for attr in [
                "nr",
                "name",
                "address_name",
                "address_company",
                "address_supplement",
                "address_street",
                "address_zipcode",
                "address_city",
                "address_country",
                "language",
            ]
        }
        data["address_country"] = str(data["address_country"])
        data["name"] = data["address_company"]
        data["invoice_via_email"] = False
        data["invoice_via_snailmail"] = False
        return data

    def get_djcrm_url(self):
        url = settings.PLUGIN_SETTINGS["pretalx_com"]["djcrm_url"]
        url += "/" if not url.endswith("/") else ""
        url += "api/customers/"
        if self.nr:
            url += self.nr + "/"
        return url

    @transaction.atomic
    def sync(self, pull=False):
        headers = {
            "Authorization": "Token "
            + settings.PLUGIN_SETTINGS["pretalx_com"]["djcrm_token"],
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        method = "POST"
        if self.nr:
            if pull:
                method = "GET"
            else:
                method = "PUT"
        response = requests.request(
            method,
            self.get_djcrm_url(),
            data=None if method == "GET" else json.dumps(self.as_dict),
            headers=headers,
        )
        response.raise_for_status()
        content = response.json()
        self.nr = content["nr"]
        if pull:
            for key, value in content.items():
                if key == "id":
                    continue
                setattr(self, key, value)
                if not self.address_street and content["address_legacy"]:
                    parts = content["address_legacy"].split("\r\n")
                    self.address_name = parts[0]
                    self.address_street = parts[1]
                    self.address_zipcode, self.address_city = parts[-1].split(
                        " ", maxsplit=1
                    )
            self.log_action(
                "pretalx.com.organiser.djcrm.pull",
                person=None,
                data={"response": content},
            )
        else:
            self.log_action(
                "pretalx.com.organiser.djcrm.push",
                person=None,
                data={"request": self.as_dict, "response": content},
            )
        self.save()


class OrganiserComProfile(LogMixin, models.Model):
    organiser = models.OneToOneField(
        to=Organiser, on_delete=models.CASCADE, related_name="com"
    )
    activations_left = models.PositiveIntegerField(null=True, blank=True)
    activations_reset_date = models.DateField(null=True, blank=True)
    discount = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="0.25 for the standard community discount, -0.42 for the 42% increase for US corps withholding 30%",
    )

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"Com profile for {self.organiser.name}, {self.activations_left} activations left until {self.activations_reset_date}"

    @property
    def block_activation(self):
        # This property is only used if activation is blocked on the event level.
        # Once the event is unlocked by other ways, it is ignored.
        return not self.activations_left


class EventComProfile(LogMixin, models.Model):
    event = models.OneToOneField(to=Event, on_delete=models.CASCADE, related_name="com")
    contact_info = models.CharField(null=True, blank=True, max_length=255)

    unlock_activation = models.BooleanField(default=False)
    skip_deletion = models.BooleanField(default=False)
    # We warn two weeks before deletion
    warned_about_deletion = models.DateTimeField(null=True, blank=True)

    discount = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="0.25 for the standard community discount, -0.42 for the 42% increase for US corps withholding 30%",
    )
    agreed_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True
    )

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"Com profile for {self.event.name}"

    @property
    def is_overdue(self):
        if self.invoiced:
            return any(
                [invoice.is_overdue for invoice in self.event.com_invoices.all()]
            )
        return False

    @property
    def paid(self):
        if self.invoiced:
            return all([invoice.paid for invoice in self.event.com_invoices.all()])
        return False

    @property
    def ignore_paid(self):
        if self.unlock_activation:
            return True
        if self.invoiced:
            return all(
                [
                    invoice.ignore_paid is True
                    for invoice in self.event.com_invoices.all()
                ]
            )
        return False

    @property
    def invoiced(self):
        invoices = getattr(self.event, "com_invoices", None)
        if invoices:
            return invoices.count()

    @cached_property
    def contact_user(self):
        with scope(event=self.event):
            for log in ActivityLog.objects.filter(event=self.event).order_by(
                "timestamp"
            ):
                if log.person:
                    return log.person

    @cached_property
    def contact(self):
        if self.contact_info:
            return self.contact_info
        if self.contact_user:
            self.contact_info = self.contact_user.email
            self.save()
            return self.contact_user.email

    @cached_property
    def can_be_deleted(self):
        # Last ditch sanity check
        if self.invoiced or self.unlock_activation or self.skip_deletion:
            return False
        if self.event.is_public:
            return False
        # cannot delete if the event is in the future and less than two years away
        today = now().date()
        if (
            self.event.date_from > today
            and self.event.date_from < today + dt.timedelta(days=2 * 365)
        ):
            return False
        last_activity = (
            ActivityLog.objects.filter(event=self.event)
            .exclude(action_type__startswith="pretalx.com")
            .order_by("-timestamp")
            .first()
        )
        if last_activity and last_activity.timestamp > now() - dt.timedelta(days=60):
            return False
        return True

    @cached_property
    def contact_name(self):
        if self.contact_user:
            return self.contact_user.name

    @cached_property
    def joined(self):
        with scope(event=self.event):
            log = (
                ActivityLog.objects.filter(
                    event=self.event, action_type="pretalx.event.create"
                ).first()
                or ActivityLog.objects.filter(event=self.event)
                .order_by("timestamp")
                .first()
            )
        return log.timestamp if log else None

    @cached_property
    def block_activation(self):
        # We forbid activations if the event is not invoiced yet (without the
        # ignore_paid override).
        if self.ignore_paid:
            return False
        return not self.invoiced

    @cached_property
    def notification_subject(self):
        return f"pretalx.com: {self.event.slug}"

    def run_notifications(self):
        """Call this from a scoped context."""
        _now = now()
        event = self.event
        if not event.settings.com_notify_new_customer:
            self.notify_new_customer()

        payment_cutoff = _now - dt.timedelta(days=40)
        send_reminders = _now.day == 1
        for invoice in event.com_invoices.all():
            if not event.settings.get(f"com_notify_new_invoice_{invoice.pk}"):
                invoice.notify_new()
            if (
                send_reminders
                and not invoice.paid
                and invoice.date < payment_cutoff.date()
                and not event.settings.get(f"com_notify_unpaid_invoice_{invoice.pk}")
            ):
                invoice.notify_unpaid()

    def _notify(self, text, subject=None, to=None, send_directly=False):
        if isinstance(to, str):
            to = [to or self.contact]
        elif isinstance(to, (list, tuple)):
            to = [t for t in to if t]
            to = to or [self.contact]
        else:
            to = [self.contact]
        reply_to = "sales@pretalx.com"

        if not send_directly:
            reply_to, to = to, [reply_to]
            reply_to = reply_to[0] if reply_to else None

        mail_send_task.apply_async(
            kwargs={
                "to": to,
                "subject": subject or self.notification_subject,
                "body": text,
                "html": None,
                "reply_to": reply_to,
                # We're not setting the event's PK, as we want to always use our own
                # email server.
            },
            ignore_result=True,
        )

    def notify_new_customer(self):
        is_repeat_customer = self.event.organiser.events.count() > 1
        if is_repeat_customer:
            # show every feature since 2 weeks before their last event
            other_events = self.event.organiser.events.exclude(pk=self.event.pk)
            last_event = other_events.order_by(
                "-date_from"
            ).first().date_from - dt.timedelta(days=14)
            other_event_str = ", ".join(str(e.name) for e in other_events)

            self._notify(
                f"""New REPEAT customer: {self.contact_name} <{self.contact}> for {str(self.event.name)}, joined on {self.joined.isoformat()}: {self.event.orga_urls.base.full()}

Previous events: {other_event_str}

Dear {self.contact_name},

thank you for using pretalx again! We're happy to have you back, and hope you'll
enjoy using pretalx for your event.

I just wanted to check if you had any questions or feedback for us, either from
your previous event or from your current one.

As you probably know, pretalx is under active development, and we've added a lot
of new features since you last used it, for example:

{get_new_features(since=last_event)}

-----

Hallo {self.contact_name},

willkommen zurück bei pretalx! Wir freuen uns, dass Sie wieder dabei sind, und
hoffen, dass Sie pretalx auch dieses Mal wieder gerne nutzen.

Ich wollte nur kurz fragen, ob Sie Fragen oder Feedback für uns haben, entweder
von Ihrem letzten oder Ihrem jetzigen Event.

Wie Sie vermutlich wissen, wird pretalx ständig weiterentwickelt, und wir haben
seit Ihrem letzten Event viele neue Funktionen hinzugefügt, zum Beispiel:

{get_new_features(lang="de", since=last_event)}

Viele Grüße
Tobias Kunze
    """,
                subject="Welcome back to pretalx!",
            )
        else:
            self._notify(
                f"""New customer: {self.contact_name} <{self.contact}> for {str(self.event.name)}, joined on {self.joined.isoformat()}: {self.event.orga_urls.base.full()}

Dear {self.contact_name},

my name is Tobias, and I'm part of the pretalx team. I saw that you recently
signed up to pretalx with {str(self.event.name)} and had a look around.

I just wanted to check if you liked our software, and if there is anything that
we could do to help you. Feel free to contact me for any feedback or questions
you have.

As you probably know, there are a bunch of other CONFTYPE events that
use pretalx, but if you'd like to see some reference events, just let me know :)

-----

Hallo {self.contact_name},

mein Name ist Tobias von pretalx. Ich habe gerade gesehen, dass Sie sich für
{str(self.event.name)} einen Account bei pretalx geklickt haben, und sich etwas
umgesehen haben.

Ich wollte nur kurz fragen, ob pretalx Ihnen gefallen hat, und ob ich irgendwie
helfen kann. Wenden Sie sich mit Feedback oder Fragen gerne immer an mich!

Wie Sie vermutlich wissen, wird pretalx schon von einigen anderen CONFTYPE-
Veranstaltungen genutzt – aber wenn Sie gerne eine Veranstaltung als Referenz
sehen wollen, lassen Sie es mich einfach wissen.

Viele Grüße
Tobias Kunze
""",
                subject="Welcome to pretalx!",
            )
        self.event.settings.com_notify_new_customer = True

    def update_invoice(self):
        for invoice in self.event.com_invoices.filter(paid=False):
            invoice.sync()

    def warn_about_deletion(self):
        if self.warned_about_deletion:
            return

        event_name = str(self.event.name)
        contact = set([self.contact, self.event.email])
        if self.contact_user:
            contact.add(self.contact_user.email)
        contact = list(contact - {None})

        self._notify(
            f"""Hi {event_name} team,

we noticed that you haven't used your pretalx account for {event_name} in a while.

To avoid cluttering pretalx.com with unused test events, we periodically delete events that haven't been used in a while.
We will delete {event_name} in two weeks, but if you want to keep it around, just log in and start using it again
– or let us know, and we'll keep it around for you.

If you have any questions, just let us know!

Best regards
the pretalx.com team""",
            subject=f"Your pretalx event {event_name} will be deleted soon",
            send_directly=True,
            to=contact,
        )

        self.warned_about_deletion = now()
        self.save()
        self.log_action("pretalx.com.event.warned_about_deletion")


class EventComInvoice(LogMixin, models.Model):
    event = models.ForeignKey(
        to=Event, on_delete=models.CASCADE, related_name="com_invoices"
    )
    amount = models.DecimalField(max_digits=7, decimal_places=2)
    number = models.CharField(max_length=30)
    ticket_price_level = models.IntegerField(null=True)
    attendee_level = models.IntegerField(null=True)
    discount = models.DecimalField(
        null=True, max_digits=5, decimal_places=4
    )  # four decimal places, one leading, so that we could say 12.25%. Between 0 and 1.
    date = models.DateField()
    paid = models.BooleanField(default=False)
    ignore_paid = models.BooleanField(default=False)
    secret = models.CharField(default=generate_secret, max_length=32)
    invoice = models.FileField(upload_to=invoice_path, max_length=240)
    user = models.ForeignKey(
        to="person.User", null=True, blank=True, on_delete=models.SET_NULL
    )

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"Invoice {self.number} for {self.event.name}"

    @property
    def is_overdue(self):
        return not self.paid and self.date + dt.timedelta(days=30) < now().date()

    @classmethod
    def create_from_data(
        cls,
        price,
        customer,
        tax_rate,
        reverse_charge,
        event,
        discount=None,
        ticket_price_level=None,
        attendee_level=None,
        user=None,
    ):
        headers = {
            "Authorization": "Token "
            + settings.PLUGIN_SETTINGS["pretalx_com"]["djcrm_token"],
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        data = {
            "date": now().date().isoformat(),
            "sepa_mandate": None,
            "contact": 1,
            "currency": "EUR",
            "customer": customer,
            "payment_terms": "30TÜberweisung",
            "text_blocks": [1, 2],
            "lines": [
                {
                    # "total_net": "375.00",
                    "costcenter": "pretalx",
                    "quantity": "1.000",
                    "single_net": str(price),
                    "tax_rate": tax_rate,
                    "text": str(event.name),
                    "title": "pretalx.com hosting services",
                    "unit": "Event",
                }
            ],
        }
        if reverse_charge:
            data["reverse_charge_vat_id"] = reverse_charge
        response = requests.post(
            cls.get_base_djcrm_url(), data=json.dumps(data), headers=headers
        )
        response.raise_for_status()
        invoice_data = response.json()
        invoice = cls(
            event=event,
            amount=price,
            number=invoice_data["nr"],
            date=now().date(),
            discount=discount,
            ticket_price_level=ticket_price_level,
            attendee_level=attendee_level,
            user=user,
        )
        invoice_file_response = requests.get(invoice_data["pdf"])
        invoice.invoice.save(
            invoice.number + ".pdf", ContentFile(invoice_file_response.content)
        )
        invoice.save()
        requests.patch(
            invoice.get_djcrm_url(),
            data=json.dumps({"status": "sent"}),
            headers=headers,
        )
        invoice.log_action("pretalx.com.invoice.created", person=user)

    @classmethod
    def get_base_djcrm_url(cls):
        url = settings.PLUGIN_SETTINGS["pretalx_com"]["djcrm_url"]
        url += "/" if not url.endswith("/") else ""
        url += "api/invoices/"
        return url

    def get_djcrm_url(self):
        url = self.get_base_djcrm_url()
        if self.number:
            url += self.number + "/"
        return url

    @transaction.atomic
    def sync(self, pull=True):
        if not pull:
            raise NotImplementedError

        headers = {
            "Authorization": "Token "
            + settings.PLUGIN_SETTINGS["pretalx_com"]["djcrm_token"],
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        response = requests.get(self.get_djcrm_url(), headers=headers)
        response.raise_for_status()
        content = response.json()
        self.amount = content["gross_total"]
        if self.paid != (content["payment_status"] == "paid"):
            self.paid = content["payment_status"] == "paid"
            self.log_action("pretalx.com.invoice.paid")
        if not self.invoice:
            invoice_file_response = requests.get(content["pdf"])
            self.invoice.save(
                self.number + ".pdf", ContentFile(invoice_file_response.content)
            )
            self.log_action("pretalx.com.invoice.fetched")
        self.save()

    def notify_new(self):
        com = get_event_com_profile(self.event)
        com._notify(
            f"""New invoice {self.number}
Amount: {self.amount}€
Date: {self.date}
Contact: {com.contact}
Event: {str(self.event.name)} ({self.event.get_date_range_display()})
URL: {self.event.orga_urls.base.full()}""",
            subject=f"New invoice: {self.amount}€ for {self.event.name}",
        )
        self.event.settings.set(f"com_notify_new_invoice_{self.pk}", True)

    def notify_unpaid(self):
        com = get_event_com_profile(self.event)
        com._notify(
            f"""Unpaid invoice {self.number} ({self.amount}), {self.date}: {com.contact} for {str(self.event.name)} ({self.event.get_date_range_display()}), {self.event.orga_urls.base.full()}

Hi,

our bookkeeping department just noticed that your invoice, {self.number} (EUR {self.amount}) is still unpaid.

Please send the payment within the next seven working days – if you have already sent the payment, thank you (and please disregard this email)!
If there is any problem with the payment that we could assist with, please let us know – we'll be happy to help.


Sehr geehrte Damen und Herren,

unsere Buchhaltung hat gerade festgestellt, dass Ihre Rechnung, {self.number} (EUR
{self.amount}), noch nicht beglichen wurde.

Bitte überweisen Sie den Betrag innerhalb der nächsten sieben Werktage – falls Sie die
Zahlung bereits getätigt haben, vielen Dank (und bitte ignorieren Sie diese E-Mail)!

Wenn es ein Problem mit der Zahlung gibt, bei dem wir helfen können, lassen Sie es uns
wissen – wir helfen gerne!
""",
            subject=f"Payment reminder for your pretalx invoice {self.number}",
            to=self.user.email if self.user else None,
        )
        self.event.settings.set(f"com_notify_unpaid_invoice_{self.pk}", True)


class BlogPost(models.Model):
    author = models.CharField(
        max_length=100, default="Tobias Kunze", null=True, blank=True
    )
    published = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    is_draft = models.BooleanField(default=False)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    content = models.TextField()
    image = models.FileField(
        upload_to="com/blog/", null=True, blank=True, max_length=240
    )
    image_title = models.CharField(
        max_length=500, help_text=_("Will be shown as alt text"), null=True, blank=True
    )
    image_caption = models.CharField(
        max_length=500,
        help_text=_("Will be shown as caption below the image"),
        null=True,
        blank=True,
    )
    image_source = models.CharField(
        max_length=500,
        help_text=_("Use markdown to include a source."),
        null=True,
        blank=True,
    )

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        ordering = ("-published",)

    def __str__(self):
        return f"Blog post: {self.title} ({self.published})"

    def get_intro(self):
        return (
            self.content.split(". ", maxsplit=1)[0].split("\n", maxsplit=1)[0]
            if self.content
            else None
        )

    def get_absolute_url(self):
        return f"https://pretalx.com/p/news/{self.slug}/"


class PretalxInstance(LogMixin, models.Model):
    id = models.CharField(unique=True, primary_key=True, max_length=32)
    name = models.CharField(null=True, blank=True, max_length=50)
    first_check = models.DateTimeField(auto_now_add=True)
    last_check = models.DateTimeField()
    last_poll = models.DateTimeField(null=True, blank=True)
    last_ip_address = models.CharField(max_length=50, null=True, blank=True)
    # Determines step back until we only check once a month
    error_count = models.IntegerField(default=0)
    # Determines if we should check at all: this might be an instance that used to
    # exist, but is now a pretalx.com alias. We want to retain old event data, but
    # not check for new events.
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.name or self.id}"

    @cached_property
    def latest_data(self):
        return self.data.order_by("datetime").last()

    def save(self, *args, **kwargs):
        if self.pk and self.latest_data:
            self.last_ip_address = self.latest_data.address or self.last_ip_address
        return super().save(*args, **kwargs)

    @transaction.atomic
    def merge_with(self, other_instance):
        # This method figures out which instance to keep by looking at which has the
        # latest data.
        own_data = self.latest_data
        other_data = other_instance.latest_data
        if own_data and not other_data:
            new = self
            old = other_instance
        elif other_data and not own_data:
            new = other_instance
            old = self
        elif (not own_data and not other_data) or (
            own_data.datetime > other_data.datetime
        ):
            new = self
            old = other_instance
        else:
            new = other_instance
            old = self

        # We can simply reassign data
        old.data.update(instance=new)
        # We have to deduplicate events
        new_events = new.events.all().values_list("slug", flat=True)
        for event in old.events.all():
            if event.slug in new_events:
                event.delete()
            else:
                event.instance = new
                event.save()
        if old.name and (not new.name or "?" in new.name or " " in new.name):
            new.name = old.name
        new.save()
        if new.first_check > old.first_check:
            PretalxInstance.objects.filter(pk=new.pk).update(
                first_check=old.first_check
            )
        old.delete()
        return new

    def update_known_events(self, force=False):
        from .utils import get_with_fallback

        if not self.is_active:
            return
        if not self.name or "?" in self.name or " " in self.name:
            return

        if not force and self.last_poll:
            # By default, add a day's timeout per error response received,
            # but still check once a month at least.
            # Do not check more often than once a day.
            min_interval = dt.timedelta(
                minutes=min(60 * 24 * (self.error_count + 1), 60 * 24 * 30)
            )
            if self.last_poll > now() - min_interval:
                return

        try:
            events = get_with_fallback(self.name, "/api/events/")
        except Exception:
            self.error_count += 1
            self.last_poll = now()
            self.save()
            return

        known_events = {event.slug: event for event in self.events.all()}

        # check if "cozyconf-2020" is in the events, as it's definitely one of ours
        # we also currently don't have huge instances apart from pretalx.com
        if self.name != "pretalx.com" and (
            len(events) > 150 or "cozyconf-2020" in known_events
        ):
            self.is_active = False
            self.name = f"{self.name} (moved to pretalx.com)"
            self.save()
            self.log_action("pretalx.com.instance.moved_to_pretalx_com")
            return

        for event in events:
            data = PretalxInstanceEvent.parse_data(event)
            if event["slug"] in known_events:
                event_obj = known_events[event["slug"]]
                dirty = False
                for key in ["date_from", "date_to", "timezone", "name"]:
                    if data[key] != getattr(event_obj, key):
                        dirty = True
                        setattr(event_obj, key, data[key])
                if dirty:
                    event_obj.save()
            else:
                instance = PretalxInstanceEvent.objects.create(instance=self, **data)
                instance.log_action("pretalx.com.event.created")

        self.last_poll = now()
        self.save()

        from .tasks import task_update_instance_version

        task_update_instance_version.apply_async(
            kwargs={"instance_id": self.pk}, ignore_result=True
        )


class PretalxInstanceEvent(LogMixin, models.Model):
    slug = models.CharField(max_length=200)
    instance = models.ForeignKey(
        to=PretalxInstance,
        on_delete=models.CASCADE,
        related_name="events",
    )

    # For legacy data reasons, all fields are nullable
    name = models.CharField(null=True, blank=True, max_length=200)
    date_from = models.DateField(null=True, blank=True)
    date_to = models.DateField(null=True, blank=True)
    timezone = models.CharField(null=True, blank=True, max_length=200)
    base_url = models.CharField(null=True, blank=True, max_length=200)

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)

    # We ignore events that aren't meant to be in stats anywhere
    ignored = models.BooleanField(default=False)

    def __str__(self):
        return f"External event {self.name} ({self.url})"

    @property
    def url(self):
        base_url = self.base_url or self.instance.name
        return f"https://{base_url}/{self.slug}/"

    @classmethod
    def parse_data(cls, data):
        # Parse JSON data from pretalx API
        return {
            "slug": data["slug"],
            "name": str(LazyI18nString(data["name"])) if "name" in data else None,
            "date_from": (
                dt.datetime.strptime(data["date_from"], "%Y-%m-%d").date()
                if "date_from" in data
                else None
            ),
            "date_to": (
                dt.datetime.strptime(data["date_to"], "%Y-%m-%d").date()
                if "date_to" in data
                else None
            ),
            "timezone": data["timezone"] if "timezone" in data else None,
            "base_url": (
                data["urls"]["base"]
                if "urls" in data and "base" in data["urls"]
                else None
            ),
        }

    def get_absolute_url(self):
        return self.base_url


class PretalxInstanceData(models.Model):
    instance = models.ForeignKey(
        to=PretalxInstance, on_delete=models.CASCADE, related_name="data"
    )
    datetime = models.DateField(auto_now_add=True)
    pretalx_version = models.CharField(max_length=15)
    data = models.TextField()

    def __str__(self):
        return f"{self.instance} data from {self.datetime}"

    @cached_property
    def json_data(self):
        return json.loads(self.data) if self.data else {}

    @cached_property
    def address(self):
        return self.json_data.get("debug", {}).get("X-Forwarded-For", "")
