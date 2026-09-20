from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Notification


@login_required
def notifications_view(request):
    """Display all notifications for the logged-in user."""
    # Fetch only notifications for the current user, newest first
    notifications = Notification.objects.filter(recipient=request.user)

    # Count unread notifications
    unread_count = notifications.filter(is_read=False).count()

    context = {
        'notifications': notifications,
        'unread_count': unread_count,
    }
    return render(request, 'notifications/notifications.html', context)


@login_required
def mark_notification_read(request, notification_id):
    """Mark a single notification as read."""
    if request.method != 'POST':
        return HttpResponseForbidden("Only POST requests are allowed.")

    notification = get_object_or_404(Notification, pk=notification_id)

    # Security check: only the recipient can mark their own notification as read
    if notification.recipient != request.user:
        return HttpResponseForbidden("You cannot mark another user's notification as read.")

    notification.is_read = True
    notification.save()

    return redirect('notifications')


@login_required
def mark_all_notifications_read(request):
    """Mark all notifications as read for the logged-in user."""
    if request.method != 'POST':
        return HttpResponseForbidden("Only POST requests are allowed.")

    # Update all unread notifications for the current user
    Notification.objects.filter(recipient=request.user, is_read=False).update(is_read=True)

    return redirect('notifications')
