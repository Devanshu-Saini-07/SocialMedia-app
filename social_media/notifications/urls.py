from django.urls import path
from . import views

urlpatterns = [
    path("", views.notifications_view, name="notifications"),
    path("<int:notification_id>/read/", views.mark_notification_read, name="mark_notification_read"),
    path("read-all/", views.mark_all_notifications_read, name="mark_all_notifications_read"),
]
