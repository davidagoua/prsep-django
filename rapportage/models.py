from django.db import models
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel

User = get_user_model()


class RapportMensuel(TimeStampedModel, models.Model):
    file = models.FileField()
    label = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.state}'


class RapportTrimestriel(TimeStampedModel, models.Model):
    file = models.FileField()
    label = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.state}'


class RapportSemestriel(TimeStampedModel, models.Model):
    file = models.FileField()
    label = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.state}'


class RapportAnnuel(TimeStampedModel, models.Model):
    file = models.FileField()
    label = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    state = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.state}'

