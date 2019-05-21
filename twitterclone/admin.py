from django.contrib import admin
from twitterclone.notification.models import Notification
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser

admin.site.register(Notification)
admin.site.register(Tweet)
admin.site.register(TwitterUser)