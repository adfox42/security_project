# sec_log/models.py

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.title
