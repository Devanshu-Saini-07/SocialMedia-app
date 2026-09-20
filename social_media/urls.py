"""
URL configuration for social_media project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("social_media.feed.urls")),  # Root URL shows home feed
    path("accounts/", include("social_media.accounts.urls")),
    path("posts/", include("social_media.posts.urls")),
    path("feed/", include("social_media.feed.urls")),  # Keep /feed/ route for compatibility
    path("interactions/", include("social_media.interactions.urls")),
    path("follows/", include("social_media.follows.urls")),
    path("notifications/", include("social_media.notifications.urls")),
    path("messaging/", include("social_media.messaging.urls")),
    path("search/", include("social_media.search.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
