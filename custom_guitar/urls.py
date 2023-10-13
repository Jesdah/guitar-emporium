from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_custom_guitar_form, name='custom')
]
