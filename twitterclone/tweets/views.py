from django.shortcuts import render, reverse, HttpResponseRedirect
from twitterclone.tweet.models import Tweet
from twitterclone.tweet.forms import TweetForm
from django.contrib.auth.decorators import login_required


@login_required()
def tweet_creation_view(request):
    html = "../templates/generic.html"
    header = "Tweet now!"
    form = None
    button_value = "Post your tweet!"
    if request.method == "POST":
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Tweet.objects.create(
                user=request.user.twitteruser,
                tweet=data["tweet"],
            )
        return HttpResponseRedirect(reverse("home"))
    else:
        form = TweetForm()
    return render(request, html, {"header": header, "form": form,
                                  "button_value": button_value})


def tweet_view(request, id):
    html = "tweet.html"
    tweet = Tweet.objects.filter(id=id)
    return render(request, html, {"tweet": tweet})