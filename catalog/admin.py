from django.contrib import admin

from .models import *


# Add simple admin to create testing object in easiest way.


class CountryAdmin(admin.ModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class PublicPlaceAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


class WorkingScheduleAdmin(admin.ModelAdmin):
    pass


class HolidayScheduleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(PublicPlace, PublicPlaceAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(WorkingSchedule, WorkingScheduleAdmin)
admin.site.register(HolidaySchedule, HolidayScheduleAdmin)
