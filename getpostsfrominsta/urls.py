from django.urls import path
from . import views

urlpatterns = [
    path('', views.getPostsFromInsta, name='getPostsFromInsta')
]