from django import template
from social_media.follows.models import Follow

register = template.Library()

@register.filter(name='is_following')
def is_following(user, profile_user):
    if not user.is_authenticated:
        return False
    return Follow.objects.filter(follower=user, following=profile_user).exists()
