from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from core.models import Profile

def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_again = request.POST['password-again']
        """
        birthday = request.POST['birthday']
        profile_img = request.FILES['profile_img']
        name = request.POST['name']
        surname = request.POST['surname']
        """

        if password != password_again:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                # TODO log user in redirect to home page
                # TODO create a new Profile object for new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user = user_model.id)
                new_profile.save()
                return redirect('home')
    else:
        return render(request, 'register.html')
