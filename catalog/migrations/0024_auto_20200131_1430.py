# Generated by Django 3.0.2 on 2020-01-31 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_auto_20200131_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='address_pattern_lat',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='address_pattern_lng',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
