from django.shortcuts import render, reverse, HttpResponseRedirect
from twitterclone.notification.forms import NotificationForm
from django.contrib.auth.models import User
from twitterclone.notification.models import Notification
from django.contrib.auth.decorators import login_required


@login_required()
def notification_view(request):
    html = "../templates/notifications.html"
    form = None
    notification = Notification.objects.all()
    return render(request, html, {"form": notification})