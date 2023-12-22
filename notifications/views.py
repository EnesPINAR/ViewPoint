from django.shortcuts import render

def notifications(request):
    return render(request, "notifications.html")