# Generated by Django 2.2.6 on 2019-10-22 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_cafe_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.Country')),
            ],
        ),
        migrations.DeleteModel(
            name='Cafe',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
