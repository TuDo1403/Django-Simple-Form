# Generated by Django 3.2.6 on 2021-10-03 02:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='submit_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
