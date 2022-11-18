from django.db import models

# Create your models here.
class Event(models.Model):
    class Meta(object):
        verbose_name='イベント'
        verbose_name_plural = 'イベント'

    def __str__(self):
        return str(self.title)

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

    staff = models.ForeignKey(
        'home.Account',
        on_delete = models.CASCADE,
        related_name = 's',
        verbose_name = 'スタッフ',
        null = True,
        blank = True
    )

    host = models.ForeignKey(
        'home.Account',
        on_delete = models.CASCADE,
        related_name = 'h',
        verbose_name = '主催者',
        null = True,
        blank = True
    )