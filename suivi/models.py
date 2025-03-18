from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model

from planification.models import Tache
from programme.models import TacheProgram

User = get_user_model()


class TDR(TimeStampedModel,models.Model):
    file = models.FileField(verbose_name='Fichier', upload_to='tdr')
    label = models.CharField(max_length=100, null=True, blank=True)
    state = models.IntegerField(default=0)
    activity = models.ForeignKey(Tache, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Activité")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.label} - {self.state}'



class CommentaireTDR(TimeStampedModel,models.Model):
    tdr = models.ForeignKey(TDR, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()


class TDRProgramme(TimeStampedModel,models.Model):
    file = models.FileField(verbose_name='Fichier', upload_to='tdr')
    label = models.CharField(max_length=100, null=True, blank=True)
    state = models.IntegerField(default=0)
    activity = models.ForeignKey(TacheProgram, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Activité")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.label} - {self.state}'