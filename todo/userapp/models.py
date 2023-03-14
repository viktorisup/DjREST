from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField('email address', unique=True)
    password = models.CharField(max_length=16)

    def __str__(self):
        return f'{self.username}'

# Create your models here.
