from django.shortcuts import render

def help(request):
    return render(request, 'help.html')
