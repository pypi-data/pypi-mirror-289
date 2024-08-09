import logging
import socket
from contextlib import suppress

from django_scopes import scope, scopes_disabled
from pretalx.celery_app import app
from pretalx.event.models import Event

from .models import PretalxInstance, PretalxInstanceData, get_event_com_profile
from .utils import get_with_fallback

logger = logging.getLogger(__name__)


@app.task(name="pretalx_com.event_notify")
def event_notify_task(*args, event: int = None, **kwargs):
    with scopes_disabled():
        event = (
            Event.objects.prefetch_related("submissions", "com", "com_invoices")
            .filter(pk=event)
            .first()
        )
        if not event:
            return

    with scope(event=event):
        com = get_event_com_profile(event)
        try:
            com.run_notifications()
        except Exception as e:
            logger.error(e)
        if event.com_invoices:
            com.update_invoice()


@app.task(name="pretalx_com.update_known_events")
def task_update_known_events(*args, instance_id: int = None, **kwargs):
    instance = PretalxInstance.objects.filter(pk=instance_id).first()
    if (
        not instance
        or not instance.name
        or "?" in instance.name
        or " " in instance.name
    ):
        return

    instance.update_known_events()

    if not instance.last_ip_address:
        with suppress(Exception):
            instance.last_ip_address = socket.gethostbyname(instance.name)


@app.task(name="pretalx_com.update_instance_version")
def task_update_instance_version(*args, instance_id: int = None, **kwargs):
    instance = PretalxInstance.objects.filter(pk=instance_id).first()
    if not instance:
        return
    latest_event = instance.events.order_by("-date_from").first()
    if latest_event:
        # try to get the pretalx version
        with suppress(Exception):
            data = get_with_fallback(
                instance.name, f"/{latest_event.slug}/schedule.xml", json=False
            )
            comment = data.split("\n")[1]
            _, version = comment.split("pretalx v")
            version = version.split(" ")[0].strip(".")
            if not version:
                return
            if instance.latest_data and instance.latest_data.pretalx_version == version:
                return
            if instance.latest_data:
                instance.log_action(
                    "pretalx.com.instance.update",
                    data={
                        "version": version,
                        "old_version": instance.latest_data.pretalx_version,
                    },
                )
            PretalxInstanceData.objects.create(
                instance=instance,
                pretalx_version=version,
                data='{"generated": "pretalx_com.task_update_known_events"}',
            )
