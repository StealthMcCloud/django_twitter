from django.urls import path
from twitterclone.notification.views import (notification_view)


urlpatterns = [
    path("notifications/", notification_view),
]