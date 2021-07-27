from django.contrib import admin

# Register your models here.
from .models import TimeTable

# Register your models here.


class TimeTableAdmin(admin.ModelAdmin):
    list_display = (
        'day',
        'product',
        'time',
    )

    ordering = ('day',)


admin.site.register(TimeTable, TimeTableAdmin)