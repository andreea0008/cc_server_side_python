from django.contrib import admin

from .models import *


class CountryAdmin(admin.ModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class SocialAdmin(admin.ModelAdmin):
    pass


class PublicPlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'public_place_city', 'public_place_category')


class LocationAdmin(admin.ModelAdmin):
    pass


class WorkingScheduleAdmin(admin.ModelAdmin):
    pass


class HolidayScheduleAdmin(admin.ModelAdmin):
    pass


class CallOperatorAdmin(admin.ModelAdmin):
    pass


class PhoneContactAdmin(admin.ModelAdmin):
    pass


class SocialInfoAdmin(admin.ModelAdmin):
    pass


class EventTypeAdmin(admin.ModelAdmin):
    pass


class MovieEventAdmin(admin.ModelAdmin):
    pass


class CurrencyAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


class LanguageMovieAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    pass


class MovieSessionAdmin(admin.ModelAdmin):
    pass


admin.site.site_header = 'Cicerone Admin Panel'

admin.site.register(Country, CountryAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(PublicPlace, PublicPlaceAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(WorkingSchedule, WorkingScheduleAdmin)
admin.site.register(HolidaySchedule, HolidayScheduleAdmin)
admin.site.register(PhoneContact, PhoneContactAdmin)
admin.site.register(SocialInfo, SocialInfoAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(MovieEvent, MovieEventAdmin)
admin.site.register(LanguageMovie, LanguageMovieAdmin)
admin.site.register(ImageEvent, ImageAdmin)

admin.site.register(MovieSession, MovieSessionAdmin)