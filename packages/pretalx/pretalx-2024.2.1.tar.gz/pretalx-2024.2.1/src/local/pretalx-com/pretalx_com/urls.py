from django.urls import include, re_path
from pretalx.event.models.event import SLUG_REGEX

from . import views

urlpatterns = [
    re_path(".update_check/", views.update_check, name="update_check"),
    re_path(r"^p/about/", views.Homepage.as_view(), name="main.root"),
    re_path(r"^p/pricing$", views.PricingView.as_view(), name="pricing"),
    re_path(r"^p/terms$", views.Terms.as_view(), name="terms"),
    re_path(r"^p/features$", views.FeatureView.as_view(), name="features"),
    re_path(r"^p/security/$", views.SecurityView.as_view(), name="security"),
    re_path(r"^p/imprint$", views.ImprintView.as_view(), name="imprint"),
    re_path(r"^p/try", views.TryView.as_view(), name="try"),
    re_path(r"^p/privacy$", views.PrivacyView.as_view(), name="privacy"),
    re_path(
        r"^(?P<event>[^/]+)/privacy",
        views.EventPrivacyView.as_view(),
        name="event.privacy",
    ),
    re_path(
        r"^p/news/(?P<slug>[A-Za-z0-9.-]+)/",
        views.BlogPostView.as_view(),
        name="blogpost",
    ),
    re_path(r"^p/news/feed$", views.BlogPostFeed(), name="blog.feed"),
    re_path(r"^p/news/$", views.BlogView.as_view(), name="blog"),
    re_path(
        f"^orga/organiser/(?P<organiser>{SLUG_REGEX})/privacy/",
        views.OrgaPrivacyView.as_view(),
        name="privacy.orga",
    ),
    re_path(
        rf"^orga/event/(?P<event>{SLUG_REGEX})/billing",
        views.BillingView.as_view(),
        name="billing",
    ),
    re_path(
        rf"^orga/event/(?P<event>{SLUG_REGEX})/support/$",
        views.Support.as_view(),
        name="support",
    ),
    re_path(r"^orga/p/blog/new/$", views.OrgaBlogView.as_view(), name="blog.create"),
    re_path(
        r"^orga/p/blog/(?P<pk>[0-9]+)/$", views.OrgaBlogView.as_view(), name="blog.view"
    ),
    re_path(r"^orga/p/blog/$", views.OrgaBlogList.as_view(), name="blog.list"),
    re_path(
        r"^orga/p/instances/stats$",
        views.OrgaInstanceStats.as_view(),
        name="instances.stats",
    ),
    re_path(
        r"^orga/p/instances/events/$",
        views.OrgaInstanceEvents.as_view(),
        name="instances.stats",
    ),
    re_path(
        r"^orga/p/instances/list/$",
        views.OrgaInstanceList.as_view(),
        name="instances.list",
    ),
    re_path(
        r"^orga/p/instances/(?P<pk>[^/]+)/$",
        views.OrgaInstanceDetail.as_view(),
        name="instances.detail",
    ),
    re_path(r"^orga/p/calendar/$", views.OrgaCalendar.as_view(), name="calendar"),
    re_path(
        r"^orga/p/maintenance/$",
        views.MaintenanceAnnouncement.as_view(),
        name="customers.maintenance",
    ),
    re_path(
        r"^orga/p/customers/$", views.CustomerList.as_view(), name="customers.list"
    ),
    re_path(r"^orga/p/reporting/$", views.Reporting.as_view(), name="reporting"),
    re_path(r"^orga/p/support/$", views.Support.as_view(), name="support"),
    re_path(r"^orga/p/business/$", views.Business.as_view(), name="business"),
    re_path(
        r"^orga/p/calculator/$",
        views.BulkBillingCalculator.as_view(),
        name="calculator",
    ),
    re_path(
        rf"^orga/p/customers/(?P<event>{SLUG_REGEX})/",
        include(
            [
                re_path(r"^$", views.CustomerDetail.as_view(), name="customers.list"),
                re_path("^invoice/new/$", views.InvoiceDetail.as_view()),
                re_path("^invoice/(?P<pk>[0-9]+)/$", views.InvoiceDetail.as_view()),
                re_path(
                    "^invoice/(?P<pk>[0-9]+)/delete/$", views.DeleteInvoice.as_view()
                ),
            ]
        ),
    ),
]
