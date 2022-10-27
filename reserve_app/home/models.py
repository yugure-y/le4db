from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    class Meta(object):
        verbose_name = "アカウント"
        verbose_name_plural = "アカウント"

    username = models.CharField(
        max_length = 50,
        verbose_name = "名前"
    )
