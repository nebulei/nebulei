from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now=True)

    