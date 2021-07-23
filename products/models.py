from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=250)
    friendly_name = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class DifficultyLevel(models.Model):
    class Meta:
        verbose_name_plural = 'Difficulty'

    BEGINNER = 'Beginner'
    ADVANCED = 'Advanced'
    DIFFICULTY_LEVEL_CHOICES = [
        (BEGINNER, 'Beginner'),
        (ADVANCED, 'Advanced')
    ]
    difficulty_level = models.CharField(max_length=25, choices=DIFFICULTY_LEVEL_CHOICES, default=BEGINNER)

    def __str__(self):
        return self.difficulty_level


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=250)
    description = models.TextField()
    tagline = models.CharField(max_length=250, null=True, blank=True)
    difficulty = models.ForeignKey('DifficultyLevel', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    number_of_sessions = models.IntegerField(validators=[MaxValueValidator(50), MinValueValidator(1)], default=10)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name