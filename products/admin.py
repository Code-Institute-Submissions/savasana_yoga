from django.contrib import admin
from .models import Product, Category, DifficultyLevel

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'image',
        'difficulty',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class DifficultyLevelAdmin(admin.ModelAdmin):
    list_display = (
        'difficulty_level',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(DifficultyLevel, DifficultyLevelAdmin)
