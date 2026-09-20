from django.db import models
from django.contrib.auth import get_user_model
from social_media.posts.models import Post

User = get_user_model()


class Notification(models.Model):
    """
    Notification model for user activity alerts.
    Types: follow, like, comment
    """

    # Notification type choices
    NOTIFICATION_TYPES = [
        ('follow', 'Follow'),
        ('like', 'Like'),
        ('comment', 'Comment'),
    ]

    recipient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications",
        help_text="User who receives the notification"
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_notifications",
        help_text="User who triggered the notification"
    )
    notification_type = models.CharField(
        max_length=20,
        choices=NOTIFICATION_TYPES,
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="notifications",
        null=True,
        blank=True,
        help_text="Related post (for like and comment notifications)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]  # Newest first

    def __str__(self):
        return f"{self.sender.username} → {self.recipient.username} ({self.notification_type})"

    def get_message(self):
        """Generate human-readable notification message."""
        if self.notification_type == 'follow':
            return f"{self.sender.username} started following you."
        elif self.notification_type == 'like':
            return f"{self.sender.username} liked your post."
        elif self.notification_type == 'comment':
            return f"{self.sender.username} commented on your post."
        return "New notification"
