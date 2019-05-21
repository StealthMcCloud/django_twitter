from django.db import models
from django.contrib.auth.models import User


class TwitterUser(models.Model):
    username = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    following = models.ManyToManyField("self", symmetrical=False, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username