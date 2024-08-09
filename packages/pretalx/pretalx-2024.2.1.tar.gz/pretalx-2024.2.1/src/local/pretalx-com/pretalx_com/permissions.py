import rules
from pretalx.person.permissions import is_administrator


@rules.predicate
def can_view_privacy(user, obj):
    if user.is_administrator:
        return True
    return obj.teams.filter(can_create_events=True, members__in=[user])


@rules.predicate
def can_view_billing(user, obj):
    if not obj or not getattr(user, "teams", None):
        return False
    return can_view_privacy(user, obj.organiser)


rules.add_perm("com.view_billing", can_view_billing | is_administrator)
rules.add_perm("com.view_privacy", can_view_privacy)
rules.add_perm("com.administer", is_administrator)
