from django.contrib.auth.models import User
from django.db import models


class Urls(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owners', null=True)
    url = models.URLField(max_length=200)
    sorturl = models.CharField(max_length=200)
    changeurl = models.URLField(max_length=200)
    counting = models.IntegerField(default=0)