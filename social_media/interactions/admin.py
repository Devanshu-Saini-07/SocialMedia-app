from django.contrib import admin
from .models import Like, Comment


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "created_at")
    search_fields = ("user__username", "post__author__username")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "content_preview", "created_at")
    search_fields = ("user__username", "post__author__username", "content")
    list_filter = ("created_at",)
    date_hierarchy = "created_at"

    def content_preview(self, obj):
        """Show first 50 characters of content."""
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content

    content_preview.short_description = "Content"
