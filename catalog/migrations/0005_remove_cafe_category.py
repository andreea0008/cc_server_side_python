# Generated by Django 2.2.6 on 2019-10-21 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20191021_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cafe',
            name='category',
        ),
    ]
