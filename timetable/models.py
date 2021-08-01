from django.db import models

from django.conf import settings

from products.models import Product



# Create your models here.


class Day(models.Model):

    DAYS_OF_THE_WEEK = [
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday')
    ]

    day = models.CharField(max_length=10, choices=DAYS_OF_THE_WEEK, default='Mon')

    def __str__(self):
        return self.day


class TimeTable(models.Model):

    class Meta:
        verbose_name_plural = 'Time Table'
        ordering = ('day',)

    day = models.ForeignKey('Day', on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    morning_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    evening_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return f'{self.product.name}'
