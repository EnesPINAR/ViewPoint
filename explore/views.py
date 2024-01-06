from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def explorePosts(request):
    return render(request, "explore.html")
