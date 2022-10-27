from django.db import models

# Create your models here.
class Event(models.Model):
    class Meta(object):
        verbose_name='イベント'
        verbose_name_plural = 'イベント'

    title = models.CharField(
        verbose_name = 'イベント名',
        max_length = 50,
    )

    date = models.DateTimeField(
        verbose_name = '日時',
    )

    place = models.CharField(
        verbose_name = '場所',
        max_length = 50,
    )

    capacity = models.IntegerField(
        verbose_name = '定員'
    )