from django.db import models


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
    # image_use = models.BooleanField('Use image', default=False)
    # image = models.ImageField('Logo', null=True)
    # cousine = models.TextField(max_length=200, null=True)

    # address
    # TODO chek it: A good rule of thumb is that you use CharField when you need to limit the maximum length, TextField otherwise. 
    # from https://stackoverflow.com/questions/7354588/django-charfield-vs-textfield
    # address = models.CharField(max_length=50, null=True)
    # address_pattern_lat = models.CharField(max_length=15, null=True)
    # address_pattern_lng = models.CharField(max_length=15, null=True)

    # socials
    # social_www = models.TextField(max_length=50, blank=True, null=True)
    # social_facebook = models.TextField(max_length=50, blank=True, null=True)
    # social_instagram = models.TextField(max_length=50, blank=True, null=True)
    # social_email = models.TextField(max_length=50, blank=True, null=True)

    # phones
    # phone_home = models.TextField(max_length=15, null=True)
    # phone_kyivstar = models.TextField(max_length=15, null=True)
    # phone_vodephone = models.TextField(max_length=15, null=True)
    # phone_lifecell = models.TextField(max_length=15, null=True)

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


# Addresses
class Address(models.Model):
    """It is for address component"""
    public_place = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, related_name='addresses')
    address = models.TextField(blank=True, null=True, max_length=50)
    lat = models.TextField(blank=True, null=True, max_length=15)
    lng = models.TextField(blank=True, null=True, max_length=15)
