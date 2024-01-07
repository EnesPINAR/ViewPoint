from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Post, Like


@login_required(login_url='login')
def LikePost(request):
    username = request.user.username
    post_id = request.GET.get('post_id')

    post = Post.objects.get(id=post_id)

    is_liked = Like.objects.filter(post_id=post_id, username=username).first()

    if is_liked == None:
        new_like = Like.objects.create(post_id=post_id, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes + 1
        post.save()
        return redirect('home')
    else:
        is_liked.delete()
        post.no_of_likes = post.no_of_likes - 1
        post.save()
        return redirect('home')
