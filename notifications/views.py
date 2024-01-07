from django.shortcuts import render
from core.models import Profile

def notifications(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, "notifications.html", {"user_profile": user_profile})