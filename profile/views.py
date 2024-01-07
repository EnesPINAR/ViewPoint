from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, auth
from core.models import Profile, Post, FollowersCount


@login_required(login_url='login')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_posts_count = len(user_posts)

    follower = request.user.username
    user = pk
    if FollowersCount.objects.filter(follower=follower, user=user):
        follow_button_text = "Unfollow"
    else:
        follow_button_text = "Follow"

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_follows = len(FollowersCount.objects.filter(follower=pk))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_posts_count': user_posts_count,
        'follow_button_text': follow_button_text,
        'user_followers': user_followers,
        'user_follows': user_follows
    }
    return render(request, 'profile.html', context)

