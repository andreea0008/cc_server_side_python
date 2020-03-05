from django.db import models
from django.db.models import CharField


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class City(models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class PublicPlace(models.Model):
    name_company = models.CharField(max_length=49)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    # TODO chek it: A good rule of thumb is that you use CharField when you need to limit the maximum length, TextField otherwise.
    # from https://stackoverflow.com/questions/7354588/django-charfield-vs-textfield

    def __str__(self):
        return self.name_company


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

    public_place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, related_name='working_days_schedule')
    day = models.CharField(max_length=9, choices=DAYS)
    work_time_from = models.TimeField()
    work_time_to = models.TimeField()
    break_time_from = models.TimeField(blank=True, null=True)
    break_time_to = models.TimeField(blank=True, null=True)

    class Meta:
        unique_together = (('public_place', 'day'))


class HolidaySchedule(models.Model):
    """Is used to extra holidays such as: New Year, Christmas, etc."""
    date = models.DateField()
    public_place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, related_name='holidays_schedule')
    work_time_from = models.TimeField()
    work_time_to = models.TimeField()
    break_time_from = models.TimeField(blank=True, null=True)
    break_time_to = models.TimeField(blank=True, null=True)


# Social Class
class Social(models.Model):
    """It is for social component"""
    SOCIAL_NETWORKS = [('facebook', 'Facebook'), ('instagram', "Instagram"), ('email', 'Email')]

    social_place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, related_name='social')
    name_social_network = models.CharField(blank=True, null=True, choices=SOCIAL_NETWORKS, max_length=20)
    link_social_network = models.TextField(blank=True, null=True)


class Phones(models.Model):
    """It's for phone component"""
    OPERATORS = [('kyivstar', "Kyivstar"), ("vodaphone", "Vodaphone")]

    social_place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, related_name='phones')
    operatorPhone = models.CharField(blank=True, null=True, choices=OPERATORS, max_length=20)
    phone = models.CharField(blank=True, null=True, max_length=20)


class Location(models.Model):
    """It's for address or location public place component"""
    public_place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, related_name="locations")
    address_location = models.TextField(blank=True, null=True)
    lat = models.TextField(blank=True, null=True, max_length=15)
    lng = models.TextField(blank=True, null=True, max_length=15)


class Comment(models.Model):
    public_place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, related_name='comment')
    comment = models.TextField(blank=False, null=False)


class CategoryEvent(models.Model):
    categoryName = models.CharField(blank=False, null=False, max_length=40)


class EventItem(models.Model):
    eventItem = models.CharField(max_length=40)

    def __str__(self):
        return self.eventItem


class Event(models.Model):
    public_place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, related_name='event')
    event_item = models.ForeignKey(EventItem, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(blank=False, null=False, max_length=150)
    description = models.TextField(blank=True, null=True)
    schedule = models.DateTimeField('when_happens')


class Movie(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='movie')
    name_movie = models.CharField(blank=False, null=False, max_length=50)
    name_movie_original = models.CharField(blank=False, null=True, max_length=50)
    description = models.TextField(blank=False, null=False, max_length=50)
    rating_imdb = models.CharField(blank=False, null=True, max_length=5)


class Actor(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='actor')
    actorName = models.CharField(blank=False, null=False, max_length=50)


class ImageEvent(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='image_event')
    image = models.ImageField(verbose_name='image_path')

