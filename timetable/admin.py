from django.contrib import admin

from .models import TimeTable, Day


class TimeTableAdmin(admin.ModelAdmin):
    list_display = (
        'day',
        'product',
        'time',
    )

    ordering = ('day',)


class DayAdmin(admin.ModelAdmin):
    list_display = (
        'day',
    )

    ordering = ('day',)

admin.site.register(Day, DayAdmin)
admin.site.register(TimeTable, TimeTableAdmin)



	

