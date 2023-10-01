from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_guitars, name='guitars'),
    path('<int:guitar_id>/', views.guitar_detail, name='guitar_detail'),
    path('add/', views.add_guitar, name='add_guitar'),
    path('edit/<int:guitar_id>/', views.edit_guitar, name='edit_guitar'),
    path('delete/<int:guitar_id>/', views.delete_guitar, name='delete_guitar'),
]
