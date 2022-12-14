# Generated by Django 4.1.2 on 2022-10-27 05:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reserve', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='event',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='e', to='event.event', verbose_name='イベント'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='u', to=settings.AUTH_USER_MODEL, verbose_name='ユーザー'),
            preserve_default=False,
        ),
    ]
