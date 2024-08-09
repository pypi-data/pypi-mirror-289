import datetime as dt

from django.core.cache import cache
from django.db.models import Count
from django.dispatch import receiver
from django.shortcuts import reverse
from django.utils.html import escape
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django_scopes import scope, scopes_disabled
from pretalx.cfp.signals import footer_link
from pretalx.common.mail import mail_send_task
from pretalx.common.models.settings import GlobalSettings
from pretalx.common.signals import (
    activitylog_display,
    activitylog_object_link,
    minimum_interval,
    periodic_task,
)
from pretalx.common.templatetags.rich_text import render_markdown
from pretalx.event.models import Event, Organiser
from pretalx.orga.signals import activate_event, nav_event, nav_global
from pretalx.person.models import User

from .models import (
    DJCRMOrganiser,
    EventComInvoice,
    EventComProfile,
    OrganiserComProfile,
    PretalxInstance,
    PretalxInstanceEvent,
    get_event_com_profile,
)
from .tasks import event_notify_task, task_update_known_events
from .utils import (
    get_deletion_candidates,
    get_monthly_report_data,
    get_weekly_report_data,
    render_report_text,
)


@receiver(footer_link)
def footer_link(sender, request, **kwargs):
    link = (
        f"/{request.event.slug}/privacy"
        if getattr(request, "event", None)
        else "/privacy"
    )
    return [{"link": link, "label": _("Privacy")}]


@receiver(activate_event)
def activate_some_events(sender, request, **kwargs):
    com = get_event_com_profile(sender)
    o_com = getattr(
        sender.organiser, "com", None
    ) or OrganiserComProfile.objects.create(organiser=sender.organiser)

    # If we manually overrode the event's permissions, we don't need to check anything.
    if com.unlock_activation:
        return

    url = reverse("plugins:pretalx_com:billing", kwargs={"event": sender.slug})
    url2 = reverse("plugins:pretalx_com:support", kwargs={"event": sender.slug})
    # First, we check if the organiser has overdue unpaid invoices. In this case, we
    # always block activation.
    if EventComInvoice.objects.filter(
        event__organiser=sender.organiser,
        paid=False,
        ignore_paid=False,
        date__lt=now() - dt.timedelta(weeks=8),
    ).exists():
        raise Exception(
            _(
                "This event is currently in trial mode. Please pay your overdue "
                "invoices to take your event public. You can always "
                "[contact our support]({url2}) for assistance."
            ).format(url=url, url2=url2)
        )

    # If the event blocks activation, we check if there is an organiser-level override.
    # The organiser-level block is *only* checked if the event can't be activated on its
    # own.
    if com.block_activation:
        if o_com.block_activation:
            raise Exception(
                _(
                    "This event is currently in trial mode. Please [sign up for the paid "
                    "version here]({url}) to take your event public. You can always "
                    "[contact our support]({url2}) for assistance."
                ).format(url=url, url2=url2)
            )

        # We set the event to be always activatable. This avoids the organiser count
        # going down twice if this event is taken down and then made public again.
        com.unlock_activation = True
        com.save()
        o_com.activations_left -= 1
        o_com.save()
        if not o_com.activations_left:
            return str(_("You have no more event activations left after this one."))
        elif o_com.activations_reset_date:
            return str(
                _("You have {number} more event activations left until {date}.")
            ).format(
                number=o_com.activations_left,
                date=o_com.activations_reset_date.strftime("%Y-%m-%d"),
            )
        else:
            return str(_("You have {number} more event activations left.")).format(
                number=o_com.activations_left,
            )


@receiver(periodic_task)
@minimum_interval(minutes_after_success=60 * 24)
def cleanup_stale_events(sender, **kwargs):
    # First, we delete events that have been marked for deletion
    # and warned over two weeks ago.
    with scopes_disabled():
        stale_events = get_deletion_candidates(for_deletion=True)
    for event in stale_events:
        with scope(event=event):
            com = get_event_com_profile(event)
            if com.can_be_deleted:
                event.shred()

    with scopes_disabled():
        # Next, reset deletion warning timestamps for events that have been
        # warned about deletion but are not part of the deletion candidates
        # anymore.
        # We do this so that these events do not accidentally get deleted
        # if they reactivate immediately after the email got sent.
        stale_events = get_deletion_candidates()
        EventComProfile.objects.filter(
            warned_about_deletion__isnull=False,
        ).exclude(
            event__in=stale_events,
        ).update(
            warned_about_deletion=None,
        )

    # Then, we send deletion warnings for events that fit the criteria.
    with scopes_disabled():
        stale_events = get_deletion_candidates().filter(
            com__warned_about_deletion__isnull=True
        )
    for event in stale_events:
        with scope(event=event):
            com = get_event_com_profile(event)
            com.warn_about_deletion()


@receiver(periodic_task)
@minimum_interval(minutes_after_success=60 * 24 * 5)
def cleanup_stale_organisers_and_users(sender, **kwargs):
    with scopes_disabled():
        orgs = (
            Organiser.objects.all()
            .annotate(event_count=Count("events"))
            .filter(event_count=0)
        )
        for org in orgs:
            org.shred()
        # delete users who have no teams and no submissions and haven't logged in in a year
        # and also have never done anything worth logging …
        # this is a very long running query.
        # TODO remove this once we have attendee accounts
        unused_users = (
            User.objects.all()
            .annotate(
                team_count=Count("teams"),
                submission_count=Count("submissions"),
                review_count=Count("reviews"),
                answer_count=Count("answers"),
                log_entry_count=Count("log_entries"),
            )
            .filter(
                team_count=0,
                submission_count=0,
                review_count=0,
                answer_count=0,
                log_entry_count=0,
            )
            .filter(last_login__lt=now() - dt.timedelta(days=365))
        )
        for user in unused_users:
            user.shred()


@receiver(nav_global)
def show_global_admin_navigation(sender, request, **kwargs):
    if request.user.is_administrator:
        return [
            {
                "label": _("Business"),
                "url": "/orga/p/reporting/",
                "active": any(
                    request.path.startswith(url)
                    for url in (
                        "/orga/p/business/",
                        "/orga/p/customers/",
                        "/orga/p/reporting/",
                        "/orga/p/calculator/",
                        "/orga/p/calendar/",
                        "/orga/p/blog/",
                    )
                ),
                "icon": "money",
                "children": [
                    {
                        "label": _("Reporting"),
                        "url": "/orga/p/reporting/",
                        "active": request.path.startswith("/orga/p/reporting/"),
                    },
                    {
                        "label": _("Customer management"),
                        "url": "/orga/p/customers/",
                        "active": request.path.startswith("/orga/p/customers/"),
                    },
                    {
                        "label": "Invoicing",
                        "url": "/orga/p/business/",
                        "active": request.path.startswith("/orga/p/business/"),
                    },
                    {
                        "label": "Bulk billing calculator",
                        "url": "/orga/p/calculator/",
                        "active": request.path.startswith("/orga/p/calculator/"),
                    },
                    {
                        "label": _("Calendar"),
                        "url": "/orga/p/calendar/",
                        "active": request.path.startswith("/orga/p/calendar/"),
                    },
                    {
                        "label": _("Blog"),
                        "url": "/orga/p/blog/",
                        "active": request.path.startswith("/orga/p/blog/"),
                    },
                ],
            },
            {
                "label": _("Instances"),
                "url": "/orga/p/instances/list/",
                "active": request.path.startswith("/orga/p/instances/"),
                "icon": "cloud",
                "children": [
                    {
                        "label": _("Instances"),
                        "url": "/orga/p/instances/list/",
                        "active": request.path.startswith("/orga/p/instances/list/"),
                        "icon": "cloud",
                    },
                    {
                        "label": _("Events"),
                        "url": "/orga/p/instances/events/",
                        "active": request.path.startswith("/orga/p/instances/events/"),
                    },
                    {
                        "label": _("Stats"),
                        "url": "/orga/p/instances/stats",
                        "active": request.path.startswith("/orga/p/instances/stats"),
                    },
                ],
            },
            {
                "label": _("Administration"),
                "url": "/orga/p/users/",
                "active": any(
                    request.path.startswith(url) for url in ("/orga/p/maintenance/",)
                ),
                "icon": "cogs",
                "children": [
                    {
                        "label": "Maintenance",
                        "url": "/orga/p/maintenance/",
                        "active": request.path.startswith("/orga/p/maintenance/"),
                        "icon": "cloud",
                    },
                ],
            },
        ]


@receiver(nav_event)
def pretalx_com_event_nav(sender, request, **kwargs):
    navs = []
    if request.user.has_perm("com.view_billing", request.event):
        url = f"/orga/event/{request.event.slug}/billing/"
        navs.append(
            {
                "label": _("Billing"),
                "url": url,
                "active": request.path.startswith(url),
                "icon": "credit-card",
            }
        )
    url = f"/orga/event/{request.event.slug}/support/"
    navs.append(
        {
            "label": _("Support"),
            "url": url,
            "active": request.path.startswith(url),
            "icon": "medkit",
        }
    )
    return navs


@receiver(periodic_task)
@minimum_interval(minutes_after_success=60 * 24)
def notify_about_customers(**kwargs):
    for event in Event.objects.all().values_list("pk", flat=True):
        event_notify_task.apply_async(kwargs={"event": event}, ignore_result=True)


@receiver(periodic_task)
@minimum_interval(minutes_after_success=60 * 24)
def update_activations_left(**kwargs):
    OrganiserComProfile.objects.filter(activations_reset_date=now().date()).update(
        activations_reset_date=None,
        activations_left=None,
    )


@receiver(periodic_task)
def look_for_new_events(**kwargs):
    """Once a week, check if known instances have added new events."""

    # Only run on Mondays
    today = now().date()
    if today.weekday() != 0:
        return

    # Already ran today
    gs = GlobalSettings()
    last_check = gs.settings.last_instance_event_check
    if last_check:
        last_check = dt.datetime.strptime(last_check, "%Y-%m-%d")
    if last_check and last_check.date() == today:
        return

    # Already running
    key_running = "pretalx_com:look_for_new_events"
    state_running = cache.get(key_running)
    if state_running:
        return

    cache.set(key_running, True, 60 * 60 * 2)  # 2 hours
    for instance in PretalxInstance.objects.all().filter(is_active=True):
        task_update_known_events.apply_async(
            kwargs={"instance_id": instance.pk}, ignore_result=True
        )

    gs.settings.last_instance_event_check = now().strftime("%Y-%m-%d")
    cache.delete(key_running)


@receiver(periodic_task)
def send_weekly_report(sender, **kwargs):
    # Monday email: new events
    today = now().date()
    if today.weekday() != 0:
        return

    # Make sure we haven't sent this email already today
    gs = GlobalSettings()
    last_report = gs.settings.last_weekly_report
    if last_report and isinstance(last_report, str):
        last_report = dt.datetime.strptime(last_report, "%Y-%m-%d")
    if last_report and last_report.date() >= today - dt.timedelta(days=6):
        return

    # Make sure new instances have been collected
    instance_check = gs.settings.last_instance_event_check
    if instance_check:
        instance_check = dt.datetime.strptime(instance_check, "%Y-%m-%d")
    if not instance_check or instance_check.date() < today - dt.timedelta(days=1):
        return

    report_data = get_weekly_report_data(current_week=False)
    text = render_report_text(report_data)

    mail_send_task.apply_async(
        kwargs={
            "to": ["sales@pretalx.com"],
            "subject": "pretalx.com weekly report",
            "body": text,
            "html": render_markdown(text),
        },
        ignore_result=True,
    )
    gs.settings.last_weekly_report = now().strftime("%Y-%m-%d")


@receiver(periodic_task)
def send_monthly_report(sender, **kwargs):
    today = now().date()
    if today.day != 1:
        return

    # Make sure we haven't sent this email already today
    gs = GlobalSettings()
    last_report = gs.settings.last_monthly_report
    if last_report and isinstance(last_report, str):
        last_report = dt.datetime.strptime(last_report, "%Y-%m-%d")
    if last_report and last_report.date() >= today - dt.timedelta(days=2):
        return

    report_data = get_monthly_report_data(current_month=False)
    text = render_report_text(report_data, interval="month")

    mail_send_task.apply_async(
        kwargs={
            "to": ["sales@pretalx.com"],
            "subject": "pretalx.com monthly report",
            "body": text,
            "html": render_markdown(text),
        },
        ignore_result=True,
    )
    gs.settings.last_monthly_report = now().strftime("%Y-%m-%d")


@receiver(nav_global)
def show_support_form(sender, request, **kwargs):
    return [
        {
            "label": _("Support"),
            "url": "/orga/p/support/",
            "active": request.path.startswith("/orga/p/support/"),
            "icon": "medkit",
        }
    ]


@receiver(nav_global)
def show_gdpr_view(sender, request, **kwargs):
    if hasattr(request, "event") or not hasattr(request, "organiser"):
        return
    if not request.user.has_perm("com.view_privacy", request.organiser):
        return
    url = f"/orga/organiser/{request.organiser.slug}/privacy/"
    return [
        {
            "label": _("Data Protection"),
            "url": url,
            "active": request.path.startswith(url),
            "icon": "lock",
        }
    ]


@receiver(signal=activitylog_display)
def pretalx_activitylog_display(sender, activitylog, **kwargs):
    event_type = activitylog.action_type
    names = {
        "pretalx.com.registration": "New sign-up",
        "pretalx.com.organiser.djcrm.pull": "Customer CRM sync (pull)",
        "pretalx.com.organiser.djcrm.push": "Customer CRM sync (push)",
        "pretalx.com.event.warned_about_deletion": "Event deletion warning",
        "pretalx.com.invoice.created": "New invoice",
        "pretalx.com.invoice.paid": "Invoice paid",
        "pretalx.com.invoice.fetched": "Invoice updated",
        "pretalx.com.instance.moved_to_pretalx_com": "Instance moved to pretalx.com",
        "pretalx.com.event.created": "New event found in the wild",
    }
    if event_type in names:
        return names.get(event_type)

    if event_type == "pretalx.com.instance.update":
        old_version = activitylog.json_data.get("old_version")
        new_version = activitylog.json_data.get("version")
        if old_version:
            return f"Instance updated from {old_version} to {new_version}"
        return f"Instance updated to {new_version}"
    return event_type


@receiver(signal=activitylog_object_link)
def pretalx_activitylog_object_link(sender, activitylog, **kwargs):
    text = ""
    link_text = ""
    url = ""
    if isinstance(activitylog.content_object, EventComProfile):
        text = _("Event")
        link_text = escape(activitylog.content_object.event.name)
        url = activitylog.content_object.event.orga_urls.base
    elif isinstance(activitylog.content_object, DJCRMOrganiser):
        text = _("Organiser")
        link_text = escape(activitylog.content_object.organiser.name)
        url = activitylog.content_object.organiser.orga_urls.base
    elif isinstance(activitylog.content_object, EventComInvoice):
        text = _("Invoice")
        link_text = escape(activitylog.content_object.number)
        url = reverse(
            "plugins:pretalx_com:billing",
            kwargs={
                "event": activitylog.content_object.event.slug,
            },
        )
    elif isinstance(activitylog.content_object, PretalxInstance):
        text = _("Instance")
        if activitylog.content_object.name:
            link_text = escape(activitylog.content_object.name)
            url = f"https://{activitylog.content_object.name}"
        elif activitylog.content_object.latest_data:
            link_text = escape(activitylog.content_object.latest_data.address)
            url = f"https://{activitylog.content_object.latest_data.address}"
    elif isinstance(activitylog.content_object, PretalxInstanceEvent):
        url = activitylog.content_object.url
        link_text = escape(activitylog.content_object.name)
        text = "Tracked event"
    if url:
        return f'{text} <a href="{url}">{link_text or url}</a>'
    if text or link_text:
        return f"{text} {link_text}"
