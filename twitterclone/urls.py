"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path

from twitterclone.authentication.urls import urlpatterns as authentication_urls
from twitterclone.notification.urls import urlpatterns as notification_urls
from twitterclone.tweet.urls import urlpatterns as tweet_urls
from twitterclone.twitteruser.urls import urlpatterns as twitteruser_urls


from twitterclone.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_view, name="home")
]

urlpatterns += authentication_urls
urlpatterns += notification_urls
urlpatterns += tweet_urls
urlpatterns += twitteruser_urls