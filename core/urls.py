from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('explore/', include('explore.urls')),
    path('help/', include('help.urls')),
    path('login/', include('login.urls')),
    path('register/', include('register.urls')),
    path('logout/', include('logout.urls')),
    path('notifications/', include('notifications.urls')),
    path('profile/<str:pk>', include('profile.urls')),
    path('follow/', include('follow.urls')),
    path('settings/', include('settings.urls')),
    path('home/', include('home.urls')),
    path('edit-profile/', include('editprofile.urls')),
    path('upload/', include('upload.urls')),
    path('like-post/', include('likepost.urls')),
    path('search/', include('search.urls')),
]
