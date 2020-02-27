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


class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(PublicPlace, PublicPlaceAdmin)
admin.site.register(WorkingSchedule, WorkingScheduleAdmin)
admin.site.register(HolidaySchedule, HolidayScheduleAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Address, AddressAdmin)
