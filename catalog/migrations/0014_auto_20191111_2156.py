# Generated by Django 2.2.6 on 2019-11-11 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_auto_20191111_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='image',
            field=models.ImageField(null=True, upload_to='', verbose_name='Logo'),
        ),
        migrations.AddField(
            model_name='cafe',
            name='image_use',
            field=models.BooleanField(default=False, verbose_name='Use image'),
        ),
    ]
