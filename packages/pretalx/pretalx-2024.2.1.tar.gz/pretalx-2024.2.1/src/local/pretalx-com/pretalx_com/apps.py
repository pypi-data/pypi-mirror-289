from django.apps import AppConfig
from django.utils.translation import gettext_lazy


class PluginApp(AppConfig):
    name = "pretalx_com"
    verbose_name = "pretalx.com"

    class PretalxPluginMeta:
        name = gettext_lazy("pretalx.com")
        author = "Tobias Kunze"
        description = gettext_lazy("The pretalx.com plugin")
        visible = False
        version = "0.0.0"
        category = "OTHER"

    def ready(self):
        from . import permissions  # NOQA
        from . import signals  # NOQA
        from . import tasks  # NOQA
