from django.urls import path
from . import views

urlpatterns = [
    path('<int:guitar_id>/', views.add_review, name='review'),
]
