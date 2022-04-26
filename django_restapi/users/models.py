from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    def __str__(self):
        return self.name

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

