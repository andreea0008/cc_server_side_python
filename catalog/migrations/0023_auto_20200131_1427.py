# Generated by Django 3.0.2 on 2020-01-31 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_holidayschedule_workingschedule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='work_every_day',
        ),
    ]
