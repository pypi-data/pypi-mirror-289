import datetime as dt

import bleach
import markdown
import requests
from django.db.models import Exists, OuterRef, Q, Subquery
from django.utils.safestring import mark_safe
from django.utils.timezone import now
from pretalx.common.models.log import ActivityLog
from publicsuffixlist import PublicSuffixList

from .models import EventComInvoice, EventComProfile, PretalxInstanceEvent

ALLOWED_TLDS = sorted(  # Sorting this list makes sure that shorter substring TLDs don't win against longer TLDs, e.g. matching '.com' before '.co'
    list({suffix.rsplit(".")[-1] for suffix in PublicSuffixList()._publicsuffix}),
    reverse=True,
)
TLD_REGEX = bleach.linkifier.build_url_re(tlds=ALLOWED_TLDS)
LINKIFIER = bleach.linkifier.Linker(url_re=TLD_REGEX, parse_email=True)


def unrestricted_markdown(text: str):
    if not text:
        return ""
    body_md = LINKIFIER.linkify(
        markdown.markdown(
            str(text),
            extensions=[
                "markdown.extensions.nl2br",
                "markdown.extensions.sane_lists",
                "markdown.extensions.tables",
                "markdown.extensions.fenced_code",
                "markdown.extensions.codehilite",
                "markdown.extensions.md_in_html",
            ],
        ),
    )
    return mark_safe(body_md)


def get_deletion_candidates(queryset=None, mode="filter", for_deletion=False):
    """Mode can be filter or exclude"""
    """If you set for_deletion, only events that have been warned > 14 days ago will be returned"""
    from pretalx.event.models import Event

    queryset = queryset or Event.objects.all().prefetch_related("com_invoices")
    invoices = EventComInvoice.objects.filter(event_id=OuterRef("pk"))
    queryset = queryset.annotate(invoiced=Exists(invoices))

    today = now().date()
    two_months_ago = today - dt.timedelta(days=60)
    try:
        two_years = today.replace(year=today.year + 2)
    except ValueError:
        # If we're on February 29th, and the next year is not a leap year, we'll get a
        # ValueError lol
        two_years = today.replace(year=today.year + 2, day=today.day - 1)

    # Only show events that are not invoiced, not public, not unlocked,
    # and in the past (or way too far in the future), and the last activity was
    # more than two months ago (so we delete after yet another month, with three months
    # of abandonment seeming sufficient).
    result = queryset.filter(
        Q(date_to__lt=today) | Q(date_to__gt=two_years),
        invoiced=False,
        is_public=False,
        com__unlock_activation=False,
        com__skip_deletion=False,
    )

    if for_deletion:
        result = result.filter(
            com__warned_about_deletion__lt=now() - dt.timedelta(days=14)
        )

    # We filter first to make this expensive subquery faster, maybe, hopefully.
    if mode == "exclude":
        result = queryset.exclude(pk__in=result.values_list("pk", flat=True))
    last_activities = (
        ActivityLog.objects.filter(event_id=OuterRef("pk"))
        .exclude(action_type__startswith="pretalx.com")
        .order_by("-id")
        .values("timestamp")[:1]
    )
    result = result.annotate(
        last_activity=Subquery(last_activities),
    )
    if mode == "filter":
        result = result.filter(last_activity__lt=two_months_ago)
    return result


def get_report_data(start, end):
    new_signups = (
        EventComProfile.objects.filter(
            created__gt=start, created__lt=end, created__isnull=False
        )
        .select_related("event")
        .order_by("created")
    )
    new_invoices = EventComInvoice.objects.filter(
        date__gte=start, date__lt=end
    ).order_by("date")
    new_events = PretalxInstanceEvent.objects.filter(
        created__gte=start, created__lt=end, created__isnull=False
    ).order_by("instance__name", "name")

    return {
        "new_signups": new_signups,
        "new_invoices": new_invoices,
        "new_events": new_events,
        "new_events_com": new_events.filter(instance__name="pretalx.com"),
        "new_invoices_sum": (
            sum([i.amount for i in new_invoices]) if new_invoices else 0
        ),
        "total_event_count": PretalxInstanceEvent.objects.all()
        .filter(ignored=False)
        .count(),
    }


def get_weekly_report_data(current_week=True):
    today = now().date()
    monday = today - dt.timedelta(days=today.weekday())
    if current_week:
        return get_report_data(monday, today + dt.timedelta(days=1))
    last_monday = monday - dt.timedelta(days=7)
    return get_report_data(last_monday, monday)


def get_monthly_report_data(current_month=True):
    today = now().date()
    first_of_month = today.replace(day=1)
    if current_month:
        return get_report_data(first_of_month, today + dt.timedelta(days=1))
    last_of_last_month = first_of_month - dt.timedelta(days=1)
    first_of_last_month = last_of_last_month.replace(day=1)
    return get_report_data(first_of_last_month, first_of_month)


def render_report_text(data, interval="week"):
    new_signups = data["new_signups"]
    new_invoices = data["new_invoices"]
    new_invoices_sum = data["new_invoices_sum"]
    new_events = data["new_events"]
    new_events_com = data["new_events_com"]

    text = ""

    if new_signups:
        text += f"There were {new_signups.count()} new signups on pretalx.com in the last {interval}:\n\n"
        for profile in new_signups:
            text += f"- {profile.event.name} ({profile.event.event.date_from} – {profile.event.date_to}) by {profile.contact_info}\n"
    else:
        text += f"There were no new signups on pretalx.com in the last {interval}.\n"

    text += "\n\n"

    if new_invoices:
        text += f"There were {new_invoices.count()} new invoices on pretalx.com in the last {interval}: for a total of {new_invoices_sum}€\n\n"
        for invoice in new_invoices:
            text += f"- {invoice.event.name}: {invoice.amount}€\n"
    else:
        text += f"There were no new invoices on pretalx.com in the last {interval}.\n"

    text += "\n\n"

    if new_events:
        text += f"There were {new_events.count()} new events ({new_events_com.count()} on pretalx.com) discovered in the last {interval}:\n\n"

        for event in new_events:
            text += f"- [{event.name}]({event.get_absolute_url()}) ({event.date_from} – {event.date_to}) on {event.instance.name}\n"
    else:
        text += f"There were no new events discovered in the last {interval}.\n"

    text += f"\nWe're up to {data['total_event_count']} events in total, globally!"
    return text


def get_with_fallback(domain, path, json=True):
    try:
        url = f"https://{domain}{path}"
        response = requests.get(url, timeout=20, verify=False)
        response.raise_for_status()
        return response.json() if json else response.text
    except Exception:
        url = f"http://{domain}{path}"
        response = requests.get(url, timeout=20, verify=False)
        response.raise_for_status()
        return response.json() if json else response.text
