# Generated by Django 4.1.2 on 2022-10-27 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='イベント名')),
                ('date', models.DateTimeField(verbose_name='日時')),
                ('place', models.CharField(max_length=50, verbose_name='場所')),
                ('capacity', models.IntegerField(verbose_name='定員')),
            ],
            options={
                'verbose_name': 'イベント',
            },
        ),
    ]