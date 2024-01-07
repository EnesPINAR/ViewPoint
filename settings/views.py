from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Profile


@login_required(login_url='login')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'settings.html', {'user_profile': user_profile})
