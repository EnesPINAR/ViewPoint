from django.contrib import admin
from django.http import HttpResponse

from . import models

admin.site.register(models.Profile)
admin.site.register(models.Post)
admin.site.register(models.Like)
admin.site.register(models.FollowersCount)
admin.site.register(models.Report)
