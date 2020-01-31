from django.contrib import admin

from .models import Cafe, WorkingSchedule, HolidaySchedule
# Add simple admin to create testing object in easiest way.

class CafeAdmin(admin.ModelAdmin):
    pass

class WorkingScheduleAdmin(admin.ModelAdmin):
    pass

class HolidayScheduleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cafe, CafeAdmin)
admin.site.register(WorkingSchedule, WorkingScheduleAdmin)
admin.site.register(HolidaySchedule, HolidayScheduleAdmin)