from django.contrib import admin

from .models import *


# Add simple admin to create testing object in easiest way.

class PublicPlaceAdmin(admin.ModelAdmin):
    pass


class WorkingScheduleAdmin(admin.ModelAdmin):
    pass


class HolidayScheduleAdmin(admin.ModelAdmin):
    pass


class SocialAdmin(admin.ModelAdmin):
    pass


class PhoneAdmin(admin.ModelAdmin):
    pass


class LocationAdmin(admin.ModelAdmin):
    pass


class CommentsAdmin(admin.ModelAdmin):
    pass


class CategoryEventAdmin(admin.ModelAdmin):
    pass


class ActorAdmin(admin.ModelAdmin):
    pass


class MovieAdmin(admin.ModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    pass


class EventItemAdmin(admin.ModelAdmin):
    pass


class ImageEventAdmin(admin.ModelAdmin):
    pass


admin.site.register(PublicPlace, PublicPlaceAdmin)
admin.site.register(WorkingSchedule, WorkingScheduleAdmin)
admin.site.register(HolidaySchedule, HolidayScheduleAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Phones, PhoneAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Comment, CommentsAdmin)
admin.site.register(CategoryEvent, CategoryEventAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventItem, EventItemAdmin)
admin.site.register(ImageEvent, ImageEventAdmin)
