from django.db import models


class Country (models.Model):
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.country


class City (models.Model):
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.city


class Category (models.Model):
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
        return '{0} {1} {2}-{3}'.format(self.location.public_place.name, self.day, self.work_time_from, self.work_time_to)


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

