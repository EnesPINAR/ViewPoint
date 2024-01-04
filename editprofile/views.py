from django.shortcuts import render


def editProfile(request):
    return render(request, 'edit-profile.html')
