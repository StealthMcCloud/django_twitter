from django.db import models
from twitterclone.twitteruser.models import TwitterUser
from twitterclone.tweet.models import Tweet


class Notification(models.Model):
    username = models.ForeignKey(
        TwitterUser, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    was_viewed = models.BooleanField(default=False)