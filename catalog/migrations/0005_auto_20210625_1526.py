# Generated by Django 3.2 on 2021-06-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_eventsession_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='finish_data_event',
        ),
        migrations.RemoveField(
            model_name='event',
            name='single_event',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_data_event',
        ),
        migrations.AlterField(
            model_name='eventsession',
            name='cost_event',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
    ]
