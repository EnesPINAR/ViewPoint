from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from core.models import Profile
from django.contrib import messages


@login_required(login_url='login')
def editProfile(request):
    user_profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        if request.FILES.get('profile-photo') is None:
            image = user_profile.profile_img
            bio = request.POST['bio']

            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.save()
        elif request.FILES.get('profile-photo') is not None:
            image = request.FILES['profile-photo']
            bio = request.POST['bio']

            user_profile.profile_img = image
            user_profile.bio = bio
            user_profile.save()
        messages.info(request, 'Changes have been saved.')
        return redirect('/profile/'+user_profile.user.username)

    return render(request, 'edit-profile.html', {'user_profile': user_profile})
