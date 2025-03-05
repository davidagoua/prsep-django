from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    contact = models.CharField(max_length=120)
