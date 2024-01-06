from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')
