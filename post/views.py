from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import User, Profile, Post

@login_required(login_url='login')
def PostSingle(request, pk):
    post = Post.objects.get(id=pk)

    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    context = {
        'post': post,
        'user_profile': user_profile
    }
    return render(request, 'post.html', context)
