from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(blank=True, null=True)