from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Follow
from social_media.notifications.models import Notification

User = get_user_model()


@login_required
def follow_user(request, username):
    """Allow the logged-in user to follow another user."""
    target_user = get_object_or_404(User, username=username)

    if request.user != target_user:
        follow, created = Follow.objects.get_or_create(follower=request.user, following=target_user)

        # Create notification only if this is a newly created follow
        if created:
            Notification.objects.create(
                recipient=target_user,
                sender=request.user,
                notification_type='follow'
            )

    return redirect("user_profile", username=target_user.username)


@login_required
def unfollow_user(request, username):
    """Allow the logged-in user to unfollow another user."""
    target_user = get_object_or_404(User, username=username)

    if request.user != target_user:
        Follow.objects.filter(follower=request.user, following=target_user).delete()

    return redirect("user_profile", username=target_user.username)


@login_required
def followers_list(request, username):
    """List of followers for a user."""
    profile_user = get_object_or_404(User, username=username)
    followers = Follow.objects.filter(following=profile_user).select_related('follower')
    return render(request, "accounts/followers.html", {
        "profile_user": profile_user,
        "followers": followers
    })


@login_required
def following_list(request, username):
    """List of users followed by a user."""
    profile_user = get_object_or_404(User, username=username)
    following = Follow.objects.filter(follower=profile_user).select_related('following')
    return render(request, "accounts/following.html", {
        "profile_user": profile_user,
        "following": following
    })
