from django.urls import path
from twitterclone.twitteruser.views import (
    signup_view, profile_view, following_or_not_view)

urlpatterns = [
    path("signup/", signup_view),
    path("followstatus/<str:username>/", following_or_not_view),
    path("<str:username>/", profile_view),
]