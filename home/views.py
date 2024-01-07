from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Post, FollowersCount
from itertools import chain


@login_required(login_url='login')
def home(request):
    user_following_list = []
    feed = []

    user_follows = FollowersCount.objects.filter(follower=request.user.username)
    for user in user_follows:
        user_following_list.append(user.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    return render(request, 'home.html', {'explore_list': feed_list})
