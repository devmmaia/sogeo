from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    """
    A Base User Class
    """
    username = models.CharField(max_length=40, unique=True)
    about = models.TextField()
    USERNAME_FIELD = 'username'
