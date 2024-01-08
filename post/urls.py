from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostSingle, name='Post')
]
