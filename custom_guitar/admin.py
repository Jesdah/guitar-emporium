from django.contrib import admin
from .models import Custom

class CustomGuitarAdmin(admin.ModelAdmin):

    list_display = ('title',
    'full_name',
    'email',
    'phone_number',
    'message',
    'make_contact',)


admin.site.register(Custom, CustomGuitarAdmin)
