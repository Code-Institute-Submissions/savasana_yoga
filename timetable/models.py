from django.db import models

from django.conf import settings

from products.models import Product

# Create your models here.

class TimeTable(models.Model):

    MON = 'Monday'
    TUE = 'Tuesday'
    WED = 'Wednesday'
    THU = 'Thursday'
    FRI = 'Friday'
    SAT = 'Saturday'
    SUN = 'Sunday'

    DAYS_OF_THE_WEEK = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday')
    ]

    day = models.CharField(max_length=10, choices=DAYS_OF_THE_WEEK, default=MON)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.SET_NULL)
    time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.day