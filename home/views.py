from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Post


@login_required(login_url='login')
def home(request):
    explore_list = Post.objects.all()
    return render(request, 'home.html', {'explore_list': explore_list})
