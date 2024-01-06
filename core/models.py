from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.TextField(blank=True, null=True)
    profile_img = models.ImageField(upload_to='images', default='/blank-profile-picture.png')

    def __str__(self):
        return self.user.username
