from django.contrib import admin
from .models import Guitar, Category

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


admin.site.register(Guitar, GuitarAdmin)
admin.site.register(Category, CategoryAdmin)
