from django.db import models


class user(models.Model):
    firstName = models.CharField(max_length=15)
    lastName = models.CharField(max_length=20)
    nickName = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    createdAt = models.DateTimeField(auto_now_add=True)
    editedAt = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.firstName
