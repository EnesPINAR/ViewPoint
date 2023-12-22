from django.http import HttpResponse
from django.shortcuts import render

def explorePosts(request):
    return render(request, "explore.html")
