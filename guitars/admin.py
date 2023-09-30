from django.contrib import admin
from .models import Guitars, Category

# Register your models here.

class GuitarAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Guitars, GuitarAdmin)
admin.site.register(Category, CategoryAdmin)
