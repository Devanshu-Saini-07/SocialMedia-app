from django.contrib import admin
from .models import Conversation, Message


@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ("id", "display_participants", "created_at")
    filter_horizontal = ("participants",)

    def display_participants(self, obj):
        return ", ".join([user.username for user in obj.participants.all()])
    display_participants.short_description = "Participants"


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("sender", "conversation", "content", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("sender__username", "content")
    date_hierarchy = "created_at"
