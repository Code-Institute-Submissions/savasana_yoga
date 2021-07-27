from django.db import models

from django.conf import settings

from products.models import Product

# Create your models here.


class TimeTable(models.Model):

    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

    DAYS_OF_THE_WEEK = [
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday')
    ]

    class Meta:
        verbose_name_plural = 'Time Table'
        ordering = ('day',)

    day = models.CharField(max_length=10, choices=DAYS_OF_THE_WEEK, default=MONDAY)
    product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return f'Name {self.product.name}'

    def __str__(self):
        return self.day
