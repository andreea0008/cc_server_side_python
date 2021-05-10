from django.db import models
from django.db.models import CharField
import PIL


class Country(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Social(models.Model):
    social_name = models.CharField(max_length=20)

    def __str__(self):
        return self.social_name


class PublicPlace(models.Model):
    name = models.CharField(max_length=49)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    poster = models.TextField(null=True, blank=True)

    @property
    def public_place_city(self):
        return self.city.city

    @property
    def public_place_country(self):
        return self.country.country

    @property
    def public_place_category(self):
        return self.category.name

    def __str__(self):
        namePublicPlace = '{0} {1}'.format(self.city, self.name)
        return namePublicPlace


class Location(models.Model):
    public_place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, related_name="locations")
    address = models.TextField(max_length=50, null=True, blank=True)
    inclusive = models.BooleanField(default=False)
    lat = models.CharField(max_length=15, null=True, blank=True)
    lng = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        result = '{0}'.format(self.address)
        return result


class PhoneContact(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="phones")
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return '{0} {1} [{2}]'.format(self.location.public_place.name, self.location.address, self.phone)


class ImagePublicPlace(models.Model):
    public_place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, related_name="image_public_place")
    image = models.TextField(null=True, blank=True)


class WorkingSchedule(models.Model):
    DAYS = (
        ('sunday', 'Sunday'),
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
    )

    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='working_days_schedule')
    day = models.CharField(max_length=9, choices=DAYS)
    work_time_from = models.TimeField()
    work_time_to = models.TimeField()
    break_time_from = models.TimeField(blank=True, null=True)
    break_time_to = models.TimeField(blank=True, null=True)

    class Meta:
        unique_together = ('location', 'day')

    @property
    def public_place_name(self):
        return self.public_place.name

    def __str__(self):
        return '{0} {1} {2}-{3}'.format(self.location.public_place.name, self.day, self.work_time_from,
                                        self.work_time_to)


class HolidaySchedule(models.Model):
    """Is used to extra holidays such as: New Year, Christmas, etc."""
    date = models.DateField()
    public_place = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='holidays_schedule')
    work_time_from = models.TimeField()
    work_time_to = models.TimeField()
    break_time_from = models.TimeField(blank=True, null=True)
    break_time_to = models.TimeField(blank=True, null=True)


class SocialInfo(models.Model):
    SOCIAL_NETWORKS = [('facebook', 'Facebook'), ('instagram', "Instagram"), ('email', 'Email')]

    public_place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, related_name='social_info')
    name_social = models.CharField(max_length=20, blank=True, null=True, choices=SOCIAL_NETWORKS)
    link = models.CharField(max_length=30, blank=True, null=True)

    @property
    def public_place_name(self):
        return self.public_place.name

    def __str__(self):
        return '{0} \'{1}\': {2}'.format(self.public_place.name, self.name_social, self.link)


class EventType(models.Model):
    type = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.type


class Currency(models.Model):
    currency_name = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return self.currency_name


class Event(models.Model):
    TYPE_MEETINGS = [('Online', 'online'), ('Offline', "offline")]
    type_of_meeting = models.CharField(max_length=20, blank=True, null=True, choices=TYPE_MEETINGS)
    type_event = models.ForeignKey(EventType, on_delete=models.CASCADE, related_name='event')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='event_location')
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='currency')
    title_event = models.CharField(max_length=40, blank=True, null=True)
    description_event = models.TextField(null=True, blank=True)
    cost_event = models.CharField(max_length=10, blank=True, null=True)
    start_data_event = models.DateTimeField(verbose_name='Start event')
    finish_data_event = models.DateTimeField(verbose_name='Finish event', null=True, blank=True)
    single_event = models.BooleanField(verbose_name='Single event', null=True, blank=True, default=True)
    poster = models.TextField(max_length=60, blank=True, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.type_event, self.title_event)

    @property
    def event_type_name(self):
        return self.type_event.type

    @property
    def location_address(self):
        return '{0}'.format(self.location.address)

    @property
    def location_lat(self):
        return '{0}'.format(self.location.lat)

    @property
    def location_lng(self):
        return '{0}'.format(self.location.lng)

    @property
    def lacation_inclusive(self):
        return self.location.inclusive

    @property
    def name_currency(self):
        return self.currency.currency_name


class ImageEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_name')
    image = models.TextField(null=True, blank=True)
    name_event = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name_event


class LanguageMovie(models.Model):
    language = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.language


class MovieEvent(Event):
    TECHNOLOGIES = [('2d', '2D'), ('IMAX', "Imax"), ('3d', '3D'), ('dbox', 'DBOX'), ('4dx', '4DX')]

    technologies = models.CharField(max_length=20, blank=True, null=True, choices=TECHNOLOGIES)

    original_name = models.CharField(max_length=50, null=True, blank=True)
    duration_movie = models.TimeField(verbose_name='Duration movie', null=True, blank=True)
    IMDB_rating = models.FloatField('IMDB', null=True, blank=True)
    link_trailer = models.TextField(verbose_name='Trailer link', blank=True, null=True)
    genre = models.CharField(max_length=60, verbose_name='Genre of movie', blank=True, null=True)
    actors = models.TextField(blank=True, null=True)
    director = models.CharField(max_length=60, null=True, blank=True)
    min_age_limit = models.PositiveSmallIntegerField(null=True, blank=True)
    countries = models.TextField(verbose_name="Countries", null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.original_name)

    @property
    def event_type_name(self):
        return self.type_event.type

    @property
    def location_address(self):
        return '{0}'.format(self.location.address)

    @property
    def location_lat(self):
        return '{0}'.format(self.location.lat)

    @property
    def location_lng(self):
        return '{0}'.format(self.location.lng)

    @property
    def lacation_inclusive(self):
        return self.location.inclusive

    @property
    def name_currency(self):
        return self.currency.currency_name

    @property
    def language_movie(self):
        return self.language.language


class Cinema(models.Model):
    movie_name = models.ForeignKey(MovieEvent, on_delete=models.CASCADE, related_name='movie_name')
    cinema_name = models.CharField(max_length=30, null=True, blank=True)


class MovieSession(models.Model):
    TECHNOLOGIES = [('2d', '2D'), ('IMAX', "Imax"), ('3d', '3D'), ('dbox', 'DBOX'), ('4dx', '4DX')]

    technologies = models.CharField(max_length=20, blank=True, null=True, choices=TECHNOLOGIES)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='cinema')
    public_place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, related_name='movie_session')
    date = models.DateTimeField(null=True, blank=True)
    ticket_link = models.TextField(null=True, blank=True)
    language = models.ForeignKey(LanguageMovie, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name='movie_currency')
    cost_event = models.CharField(max_length=10, blank=True, null=True)

    @property
    def currency_name(self):
        return self.currency.currency_name

    def __str__(self):
        return '{0} |      {1}     |      [{2} | {3}]'.format(self.cinema.cinema_name, self.public_place.name,
                                              self.technologies, self.date)

