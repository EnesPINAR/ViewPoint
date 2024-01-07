from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from core.models import Profile, Post


@login_required(login_url='login')
def upload(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('post-photo')
        caption = request.POST['caption']

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('home')
    else:
        return render(request, 'upload.html', {'user_profile': user_profile})
