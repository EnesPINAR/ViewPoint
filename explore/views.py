from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import User, Profile, Post


@login_required(login_url='login')
def explorePosts(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    explore_list = Post.objects.filter(is_active=True)
    return render(request, "explore.html", {'user_profile': user_profile, 'explore_list': explore_list})
