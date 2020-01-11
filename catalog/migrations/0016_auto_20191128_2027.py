# Generated by Django 2.2.6 on 2019-11-28 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_cafe_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='break_hour_in_weekend_from',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='break_hour_in_weekend_to',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='break_hour_in_weekend_use',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='break_hour_in_workdays_from',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='break_hour_in_workdays_to',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='break_hour_in_workdays_use',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='work_every_day_break_from',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='work_every_day_break_to',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='work_every_day_from',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='work_every_day_to',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='work_hour_in_weekday_from',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='work_hour_in_weekday_to',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='work_hour_in_workdays_from',
        ),
        migrations.RemoveField(
            model_name='cafe',
            name='work_hour_in_workdays_to',
        ),
    ]
