from django.urls import path
from . import views

app_name = "interactions"

urlpatterns = [
    path("post/<int:post_id>/like/", views.toggle_like, name="toggle_like"),
    path("post/<int:post_id>/comment/", views.add_comment, name="add_comment"),
    path("comment/<int:comment_id>/delete/", views.delete_comment, name="delete_comment"),
]
