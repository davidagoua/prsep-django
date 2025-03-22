from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel

User = get_user_model()



class TypeRapport(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label


class Rapport(TimeStampedModel, models.Model):

    type_choices = models.TextChoices('type', ['Mensuel','Trimestriel','Semestriel','Annuel','Spécifique','Autres'])

    file = models.FileField(verbose_name='Fichier', upload_to='rapports')
    label = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.IntegerField(default=0)
    type = models.CharField(max_length=100, null=True, blank=True, choices=type_choices)

    def __str__(self):
        return f'{self.user.username} - {self.state}'


