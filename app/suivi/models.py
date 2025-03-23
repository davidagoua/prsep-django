from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.dispatch import receiver
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


@receiver(models.signals.post_save, sender=TDR)
def tdr_post_save(sender, instance, created, **kwargs):
    if not created:
        channel_layer = get_channel_layer()
        channel_name = f'tdr_{instance.id}'
        async_to_sync(channel_layer.group_send)(
            channel_name,
            {
                'type': 'tdr_update',
                'data': {
                    'id': instance.id,
                    'state': instance.state
                }
            }
        )
        