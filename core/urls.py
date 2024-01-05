from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('explore/', include('explore.urls')),
    path('help/', include('help.urls')),
    path('login/', include('login.urls')),
    path('notifications/', include('notifications.urls')),
    path('profile/', include('profile.urls')),
    path('register/', include('register.urls')),
    path('settings/', include('settings.urls')),
    path('home/', include('home.urls')),
    path('edit-profile/', include('editprofile.urls')),
]