from django.db import models
from django.contrib.auth.models import AbstractUser



class Departement(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class User(AbstractUser):
    contact = models.CharField(max_length=120)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE, null=True, blank=True)





