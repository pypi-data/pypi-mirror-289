import datetime as dt

from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.utils.translation import override

LATEST_VERSION = "2024.2.0"
DEV_VERSION = "2024.3.0.dev0"
UP_TO_DATE_VERSIONS = [
    LATEST_VERSION,
    DEV_VERSION,
]
NEW_FEATURES = [
    (
        _(
            "Content languages can now be configured independently from the interface language, so you can have proposals in more languages than the interface is available in."
        ),
        dt.date(2022, 12, 23),
    ),
    (_("Better handling of teams"), dt.date(2023, 3, 20)),
    (
        _(
            "If you use room availabilities, then speakers can only select availabilities where any room is available"
        ),
        dt.date(2023, 4, 20),
    ),
    (
        _(
            "If you use anonymisation, you can now see at a glance which proposals have been anonymised / reviewed for containing personal information"
        ),
        dt.date(2023, 5, 20),
    ),
    (
        _(
            "During the CfP, submitters can now save their proposals as drafts and continue editing them later, and you can send reminders to people with draft proposals to prompt them to submit them closer to the deadline"
        ),
        dt.date(2023, 6, 20),
    ),
    (
        _(
            "We have a new schedule editor that is much easier to use, especially with shorter talks, and looks just like the public schedule for a better overview"
        ),
        dt.date(2023, 8, 5),
    ),
    (
        _(
            "Tracks can now be ordered, and will show up in that order in the schedule legend."
        ),
        dt.date(2023, 9, 10),
    ),
    (
        _(
            "You can now customize how many lines you see in lists on all organiser pages, so if your internet is slow, you can reduce the page size, or increase it to see more at a glance."
        ),
        dt.date(2023, 9, 13),
    ),
    (
        _(
            "Speakers and organisers will now be warned when they try to close a tab or navigate away from a page with unsaved changes."
        ),
        dt.date(2023, 10, 3),
    ),
    (
        _(
            "The schedule editor can now be printed (as all irrelevant UI elements are hidden in the print view). This is especially useful if you want to print the schedule of a single room!"
        ),
        dt.date(2023, 10, 28),
    ),
    (
        _(
            "There are now even more email placeholders, and they are easier to add (just click on the placeholder you want to add in the sidebar). You can also see an explanation and an example for every placeholder, and of course a preview before sending emails."
        ),
        dt.date(2023, 11, 15),
    ),
    (
        _(
            "Emails can now be sent both per-speaker and per-proposal, and pretalx will try to merge them if possible (so no speaker will get the same email five times, just because they have five proposals)."
        ),
        dt.date(2023, 11, 15),
    ),
    (
        _(
            "Pretalx is now available in Dutch and Italian, thanks to the amazing work of our community!"
        ),
        dt.date(2024, 2, 16),
    ),
    (
        _("Reviewers can now review all proposals at once on the bulk review page."),
        dt.date(2024, 2, 1),
    ),
    (
        _(
            "There is now a global search box in the sidebar, so you can find every event, speaker or proposal that you have access to, no matter where you are."
        ),
        dt.date(2024, 2, 11),
    ),
    (
        _(
            "If you mark talks as 'pending accepted', you can already schedule them in the schedule editor, so you can see how they fit in the schedule before you make your final programme decisions."
        ),
        dt.date(2024, 4, 22),
    ),
]


def get_new_features(lang="en", since=None):
    since = since or now().date() - dt.timedelta(days=6 * 30)
    with override(lang):
        return "\n".join(
            ["- " + feature[0] for feature in NEW_FEATURES if feature[1] >= since]
        )
