from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at', 'updated_at')
    list_filter  = ('author', 'created_at')
    search_fields = ('author__username', 'content')
