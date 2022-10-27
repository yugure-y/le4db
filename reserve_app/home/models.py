from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Account(AbstractUser):
    class Meta(object):
        verbose_name = 'アカウント'
        verbose_name_plural = 'アカウント'