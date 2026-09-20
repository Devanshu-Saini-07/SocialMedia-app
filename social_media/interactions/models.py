from django.db import models
from django.contrib.auth import get_user_model
from social_media.posts.models import Post

User = get_user_model()


class Like(models.Model):
    """
    A user can like a post.
    * Unique constraint ensures one like per user per post.
    * Ordered by newest first.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="likes",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="likes",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Prevent duplicate likes: one user can like a post only once
        constraints = [
            models.UniqueConstraint(
                fields=["user", "post"],
                name="unique_user_post_like",
            ),
        ]
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user.username} → {self.post.pk}"


class Comment(models.Model):
    """
    A user can comment on a post.
    * Content is required (non-empty).
    * Ordered by newest first (for display).
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.user.username} on post {self.post.pk}"
