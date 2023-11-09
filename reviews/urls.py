from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<int:guitar_id>/', views.add_review, name='add_review'),
]
