import copy
import json
from contextlib import suppress
from zoneinfo import ZoneInfo

from csp.decorators import csp_exempt, csp_replace
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.syndication.views import Feed
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils import feedgenerator
from django.utils.decorators import method_decorator
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, FormView, ListView, TemplateView
from pretalx.common.mail import mail_send_task

from pretalx_com.forms import ContactForm, RegistrationForm, SupportForm
from pretalx_com.models import BlogPost, PretalxInstance, PretalxInstanceData
from pretalx_com.prices import PRICES
from pretalx_com.utils import unrestricted_markdown
from pretalx_com.versions import LATEST_VERSION, UP_TO_DATE_VERSIONS


class Homepage(TemplateView):
    template_name = "pretalx_com/index.html"


class PrivacyView(TemplateView):
    template_name = "pretalx_com/privacy.html"


class EventPrivacyView(TemplateView):
    template_name = "pretalx_com/privacy_event.html"


class Terms(TemplateView):
    template_name = "pretalx_com/terms.html"


class PricingView(TemplateView):
    template_name = "pretalx_com/pricing.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prices"] = copy.deepcopy(PRICES)
        return context

    def post(self, request, **kwargs):
        if request.POST["submit"] == "test":
            return redirect("/p/try?mode=test")
        return redirect(
            f'/p/try?attendees={request.POST.get("attendees", 0)}&tickets={request.POST.get("tickets", 0)}'
        )


class SecurityView(TemplateView):
    template_name = "pretalx_com/security.html"


class ImprintView(TemplateView):
    template_name = "pretalx_com/imprint.html"


@method_decorator(
    csp_replace(IMG_SRC="'self' https://img.pretalx.com"), name="dispatch"
)
class FeatureView(FormView):
    template_name = "pretalx_com/features.html"
    form_class = ContactForm

    def form_valid(self, form):
        text = "Sales\n\n"
        time = now().astimezone(ZoneInfo("Europe/Berlin")).strftime("%Y-%m-%d %H:%M")
        text += f"Created on: {time} (Europe/Berlin)\n\n"
        text += f"Event: {form.cleaned_data['event']}\n\n"
        text += f'E-mail: {form.cleaned_data["email"]}' + "\n"
        text += "------\n\n"
        text += f'{form.cleaned_data["message"]}'
        mail_send_task.apply_async(
            kwargs={
                "to": ["sales@pretalx.com"],
                "subject": "Your pretalx question",
                "body": text,
                "html": None,
                "reply_to": form.cleaned_data["email"],
                "event": None,
            },
            ignore_result=True,
        )
        return redirect("/p/features")

    def form_invalid(self, form):
        return redirect("/p/features")


class TryView(FormView):
    form_class = RegistrationForm
    template_name = "pretalx_com/try.html"

    def get_form_kwargs(self):
        result = super().get_form_kwargs()
        if not self.request.user.is_anonymous:
            result["user"] = self.request.user
        return result

    @transaction.atomic
    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend="django.contrib.auth.backends.ModelBackend")
        user.log_action("pretalx.com.registration", person=user)
        messages.success(
            self.request,
            _(
                "Welcome! Now you can create your event, and then you are ready to take a look around! "
                "Please note that we reserve the right to remove your event at any time within your trial period."
            ),
        )

        queryparams = {
            key: self.request.GET.get(key)
            for key in ["attendees", "tickets"]
            if key in self.request.GET
        }
        if queryparams:
            organiser = user.teams.first().organiser
            with suppress(Exception):
                organiser.settings.registration_attendees = int(
                    queryparams["attendees"]
                )
                organiser.settings.registration_tickets = int(queryparams["tickets"])
        return redirect("orga:event.create")


class BlogView(ListView):
    template_name = "pretalx_com/blog.html"
    model = BlogPost
    context_object_name = "posts"
    paginate_by = 5

    def get_queryset(self):
        return BlogPost.objects.filter(is_draft=False)


class BlogPostView(DetailView):
    template_name = "pretalx_com/blogpost.html"
    model = BlogPost

    @csp_exempt
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["rendered"] = unrestricted_markdown(self.get_object().content)
        return context

    def get_queryset(self):
        if not self.request.user.is_anonymous and self.request.user.is_administrator:
            return BlogPost.objects.all()
        if self.request.GET.get("letmesee", "") == "👀":
            return BlogPost.objects.all()
        return BlogPost.objects.filter(is_draft=False)


class BlogPostFeed(Feed):
    feed_type = feedgenerator.Atom1Feed
    title = "pretalx.com"
    link = "/p/news/feed.atom"
    description = "Updates on the pretalx project: release notification and general announcements."

    def items(self):
        return BlogPost.objects.filter(is_draft=False)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.get_intro() + " …"

    def item_pubdate(self, item):
        return item.published

    def item_author_name(self, item):
        return item.author


class Support(FormView):
    template_name = "pretalx_com/support.html"
    form_class = SupportForm

    def get_form_kwargs(self, *args, **kwargs):
        result = super().get_form_kwargs(*args, **kwargs)
        initial = result.get("initial", dict())
        initial["email"] = self.request.user.email
        result["initial"] = initial
        return result

    def form_valid(self, form):
        try:
            subject = "[pretalx] Your pretalx support request"
            text = ""

            event = getattr(self.request, "event", None)
            if event:
                subject = f"{subject} ({event.name})"
                text += (
                    f"Created for event {event.name}: {event.orga_urls.base.full()}\n\n"
                )
                time = (
                    now()
                    .astimezone(ZoneInfo("Europe/Berlin"))
                    .strftime("%Y-%m-%d %H:%M")
                )
                text += f"Created on: {time} (Europe/Berlin)\n\n"

            text += f'Contact method: {form.cleaned_data["contact_method"]}' + "\n"
            text += f'E-mail: {form.cleaned_data["email"]}' + "\n"
            text += f'Phone: {form.cleaned_data["phone"]}' + "\n"
            text += f'Time: {form.cleaned_data["time"]}' + "\n\n"
            text += "------\n\n"
            text += f'{form.cleaned_data["message"]}'

            mail_send_task.apply_async(
                kwargs={
                    "to": ["support@pretalx.com"],
                    "subject": subject,
                    "body": text,
                    "html": None,
                    "reply_to": form.cleaned_data["email"],
                },
                ignore_result=True,
            )
            messages.success(
                self.request, _("Your support request has been sent – we are on it!")
            )
        except Exception:
            messages.error(
                self.request,
                _(
                    "The sending of your support request failed – please send us an email to support@pretalx.com instead."
                ),
            )
        if event:
            return redirect(event.orga_urls.base)
        return redirect("/orga/")


@csrf_exempt
def update_check(request):
    """
    check_payload = {
        'id': gs.settings.update_check_id,
        'version': pretalx_version,
        'events': {
            'total': Event.objects.count(),
            'public': Event.objects.filter(is_public=True).count(),
        },
        'plugins': [
            {
                'name': p.module,
                'version': p.version
            } for p in get_all_plugins()
        ]
    }
    """
    if request.method != "POST":
        return JsonResponse({})
    check_payload = json.loads(request.body.decode())
    check_version = check_payload.get("version", "")
    response = {
        "version": {
            "latest": LATEST_VERSION,
            "updatable": check_version not in UP_TO_DATE_VERSIONS,
            "yours": check_payload["version"],
        },
        "plugins": {},  # TODO: Check plugin updates
    }
    instance = PretalxInstance.objects.filter(id=check_payload["id"]).first()
    ip_address = request.headers.get("X-Forwarded-For")
    if not instance and ip_address:
        # Let's see if we have another instance with the same IP address; if so, and if
        # the other instance is also a new/empty instance, we'll assume this is the same.
        instance = PretalxInstance.objects.filter(
            last_ip_address=ip_address, name__isnull=True
        ).first()
    if not instance:
        instance = PretalxInstance.objects.create(
            id=check_payload["id"],
            last_check=now(),
            last_ip_address=ip_address,
        )
    check_payload["debug"] = dict(request.headers)
    PretalxInstanceData.objects.create(
        instance=instance,
        pretalx_version=check_payload["version"],
        data=json.dumps(check_payload),
    )
    instance.last_check = now()
    instance.save()
    return JsonResponse(response)
