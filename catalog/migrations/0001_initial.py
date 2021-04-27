# Generated by Django 3.2 on 2021-04-27 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinema_name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency_name', models.CharField(blank=True, max_length=3, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_meeting', models.CharField(blank=True, choices=[('Online', 'online'), ('Offline', 'offline')], max_length=20, null=True)),
                ('title_event', models.CharField(blank=True, max_length=40, null=True)),
                ('description_event', models.TextField(blank=True, null=True)),
                ('cost_event', models.CharField(blank=True, max_length=10, null=True)),
                ('start_data_event', models.DateTimeField(verbose_name='Start event')),
                ('finish_data_event', models.DateTimeField(blank=True, null=True, verbose_name='Finish event')),
                ('single_event', models.BooleanField(blank=True, default=True, null=True, verbose_name='Single event')),
                ('poster_event', models.ImageField(upload_to='catalog/images/events')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency', to='catalog.currency')),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Image of event')),
                ('name_event', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(blank=True, max_length=50, null=True)),
                ('inclusive', models.BooleanField(default=False)),
                ('lat', models.CharField(blank=True, max_length=15, null=True)),
                ('lng', models.CharField(blank=True, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PublicPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=49)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.city')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.country')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MovieEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='catalog.event')),
                ('technologies', models.CharField(blank=True, choices=[('2d', '2D'), ('IMAX', 'Imax'), ('3d', '3D'), ('dbox', 'DBOX'), ('4dx', '4DX')], max_length=20, null=True)),
                ('original_name', models.CharField(blank=True, max_length=50, null=True)),
                ('duration_movie', models.TimeField(blank=True, null=True, verbose_name='Duration movie')),
                ('IMDB_rating', models.FloatField(blank=True, null=True, verbose_name='IMDB')),
                ('link_trailer', models.TextField(blank=True, null=True, verbose_name='Trailer link')),
                ('genre', models.CharField(blank=True, max_length=60, null=True, verbose_name='Genre of movie')),
                ('actors', models.TextField(blank=True, null=True)),
                ('director', models.CharField(blank=True, max_length=60, null=True)),
                ('min_age_limit', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('countries', models.TextField(blank=True, null=True, verbose_name='Countries')),
            ],
            bases=('catalog.event',),
        ),
        migrations.CreateModel(
            name='SocialInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_social', models.CharField(blank=True, choices=[('facebook', 'Facebook'), ('instagram', 'Instagram'), ('email', 'Email')], max_length=20, null=True)),
                ('link', models.CharField(blank=True, max_length=30, null=True)),
                ('public_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_info', to='catalog.publicplace')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='catalog.location')),
            ],
        ),
        migrations.CreateModel(
            name='MovieSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technologies', models.CharField(blank=True, choices=[('2d', '2D'), ('IMAX', 'Imax'), ('3d', '3D'), ('dbox', 'DBOX'), ('4dx', '4DX')], max_length=20, null=True)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('ticket_link', models.TextField(blank=True, null=True)),
                ('cost_event', models.CharField(blank=True, max_length=10, null=True)),
                ('cinema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cinema', to='catalog.cinema')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_currency', to='catalog.currency')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.languagemovie')),
                ('public_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_session', to='catalog.publicplace')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='public_place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='catalog.publicplace'),
        ),
        migrations.CreateModel(
            name='HolidaySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('work_time_from', models.TimeField()),
                ('work_time_to', models.TimeField()),
                ('break_time_from', models.TimeField(blank=True, null=True)),
                ('break_time_to', models.TimeField(blank=True, null=True)),
                ('public_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='holidays_schedule', to='catalog.location')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_location', to='catalog.location'),
        ),
        migrations.AddField(
            model_name='event',
            name='type_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='catalog.eventtype'),
        ),
        migrations.CreateModel(
            name='WorkingSchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('sunday', 'Sunday'), ('monday', 'Monday'), ('tuesday', 'Tuesday'), ('wednesday', 'Wednesday'), ('thursday', 'Thursday'), ('friday', 'Friday'), ('saturday', 'Saturday')], max_length=9)),
                ('work_time_from', models.TimeField()),
                ('work_time_to', models.TimeField()),
                ('break_time_from', models.TimeField(blank=True, null=True)),
                ('break_time_to', models.TimeField(blank=True, null=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='working_days_schedule', to='catalog.location')),
            ],
            options={
                'unique_together': {('location', 'day')},
            },
        ),
        migrations.AddField(
            model_name='cinema',
            name='movie_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_name', to='catalog.movieevent'),
        ),
    ]
