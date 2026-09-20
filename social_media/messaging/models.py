from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Conversation(models.Model):
    """
    Conversation model representing a 1-to-1 chat between two users.
    """
    participants = models.ManyToManyField(User, related_name="conversations")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        usernames = ", ".join([user.username for user in self.participants.all()])
        return f"Conversation: {usernames}"

    def get_other_user(self, current_user):
        """Helper method to return the other participant in the 1-to-1 conversation."""
        return self.participants.exclude(id=current_user.id).first()

    def get_last_message(self):
        """Helper method to get the latest message."""
        return self.messages.last()


class Message(models.Model):
    """
    Message model for individual chat messages within a conversation.
    """
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages"
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_messages"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]  # Oldest to newest for natural chat view

    def __str__(self):
        return f"{self.sender.username}: {self.content[:30]}"
