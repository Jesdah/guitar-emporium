from django.urls import path
from . import views

urlpatterns = [
    # path('<int:guitar_id>/', views.view_review, name='view_review'),
    path('add_review/<int:guitar_id>/', views.add_review, name='add_review'),
]
