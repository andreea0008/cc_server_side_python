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


class PublicPlace(models.Model):
    name = models.CharField(max_length=49)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        namePublicPlace = '{0} {1}'.format(self.city, self.name)
        return namePublicPlace


class Location(models.Model):
    publicPlace = models.ForeignKey(PublicPlace, on_delete=models.CASCADE, null=True)
    address = models.TextField(max_length=50, null=True, blank=True)
    lat = models.CharField(max_length=15, null=True, blank=True)
    lng = models.CharField(max_length=15, null=True, blank=True)


class Cafe(models.Model):
    name_company = models.CharField(max_length=49)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    image_use = models.BooleanField('Use image', default=False)
    image = models.ImageField('Logo', null=True)
    cousine = models.TextField(max_length=200, null=True)

    #address
    # TODO chek it: A good rule of thumb is that you use CharField when you need to limit the maximum length, TextField otherwise. 
    # from https://stackoverflow.com/questions/7354588/django-charfield-vs-textfield
    address = models.CharField(max_length=50, null=True)
    address_pattern_lat = models.CharField(max_length=15, null=True)
    address_pattern_lng = models.CharField(max_length=15, null=True)

    #socials
    social_www = models.TextField(max_length=50, blank=True, null=True)
    social_facebook = models.TextField(max_length=50, blank=True, null=True)
    social_instagram = models.TextField(max_length=50, blank=True, null=True )
    social_email = models.TextField(max_length=50, blank=True, null=True)

    #phones
    phone_home = models.TextField(max_length=15, null=True)
    phone_kyivstar = models.TextField(max_length=15, null=True)
    phone_vodephone = models.TextField(max_length=15, null=True)
    phone_lifecell = models.TextField(max_length=15, null=True)

    #work hours
    # work_every_day = models.BooleanField(default=False)

    #SCHEDULE
    # schedule = models.TextField(max_length=400, blank=True, null=True)
    # s = ListFi

    '''
    #IF WORKS EVERY DAY
    work_every_day_from = models.TimeField("From", null=True)
    work_every_day_to = models.TimeField('To', null=True)
    work_every_day_break_from = models.TimeField('Break_from', null=True)
    work_every_day_break_to = models.TimeField('Break_to', null=True)

    #IF NOT WORK EVERY DAY FROM MONDAY TO FRIDAY
    work_hour_in_workdays_from = models.TimeField('From_in_workdays', null=True)
    work_hour_in_workdays_to = models.TimeField('To_in_workdays', null=True)
    break_hour_in_workdays_use = models.BooleanField(default=False)
    break_hour_in_workdays_from = models.TimeField('Break_from_in_workdays', null=True)
    break_hour_in_workdays_to = models.TimeField('Break_to_in_workdays', null=True)

    #IF NOT WORK EVERY DAY IN WEEKDAYS
    work_hour_in_weekday_from = models.TimeField('From_in_weekend', null=True)
    work_hour_in_weekday_to = models.TimeField('To_in_weekend', null=True)
    break_hour_in_weekend_use = models.BooleanField(default=False)
    break_hour_in_weekend_from = models.TimeField('Break_from_in_weekend', null=True)
    break_hour_in_weekend_to = models.TimeField('Break_to_in_weekend', null=True)
    '''

    #TAG
    #tags = models.TextField("TAGS", max_length=150)


    def __unicode__(self):
        return '%s: %s, %s'(self.country, self.city.name, self.category)

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

    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='working_days_schedule')
    day = models.CharField(max_length=9, choices=DAYS)
    work_time_from = models.TimeField()
    work_time_to = models.TimeField()
    break_time_from = models.TimeField(blank=True, null=True)
    break_time_to = models.TimeField(blank=True, null=True)

    class Meta:
        unique_together = (('cafe', 'day'))


class HolidaySchedule(models.Model):
    """Is used to extra holidays such as: New Year, Christmas, etc."""
    date = models.DateField()
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name='holidays_schedule')
    work_time_from = models.TimeField()
    work_time_to = models.TimeField()
    break_time_from = models.TimeField(blank=True, null=True)
    break_time_to = models.TimeField(blank=True, null=True) 
