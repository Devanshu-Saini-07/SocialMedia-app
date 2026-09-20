from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Follow(models.Model):
    """
    Follow model connecting follower and following users.
    * follower: user who clicks follow
    * following: user who is being followed
    """
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="followers",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["follower", "following"],
                name="unique_follower_following",
            ),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
