# Generated by Django 4.1.2 on 2022-10-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(verbose_name='トークン')),
                ('accepted', models.BooleanField(verbose_name='受付済')),
            ],
            options={
                'verbose_name': '予約',
                'verbose_name_plural': '予約',
            },
        ),
    ]