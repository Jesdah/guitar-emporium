from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_guitars, name='guitars'),
    path('<int:guitar_id>/', views.guitar_detail, name='guitar_detail'),
    # path('add/', views.add_product, name='add_product'),
    # path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    # path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
