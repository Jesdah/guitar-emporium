from django.contrib import admin
from .models import Reviews


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('guitar', 'review', 'post_date')
    search_fields = ['guitar', 'review', 'post_date']
