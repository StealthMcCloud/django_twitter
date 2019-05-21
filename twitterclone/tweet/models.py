from django.db import models
from twitterclone.twitteruser.models import TwitterUser
from django.utils import timezone


class Tweet(models.Model):
    user = models.ForeignKey(
        TwitterUser, on_delete=models.CASCADE)
    tweet = models.CharField(max_length=140)
    date = models.DateTimeField(default=timezone.now)