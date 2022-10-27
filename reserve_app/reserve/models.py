from django.db import models

# Create your models here.
class Reservation(models.Model):
    class Meta(object):
        verbose_name = '予約'
        verbose_name_plural = '予約'
    
    user = models.ForeignKey(
        'home.Account',
        on_delete = models.CASCADE,
        related_name = 'u',
        verbose_name = 'ユーザー',
    )

    event = models.ForeignKey(
        'event.Event',
        on_delete = models.CASCADE,
        related_name = 'e',
        verbose_name = 'イベント',
    )

    token = models.UUIDField(
        verbose_name = 'トークン',
        max_length = 50,
    )

    accepted = models.BooleanField(
        verbose_name = '受付済'
    )