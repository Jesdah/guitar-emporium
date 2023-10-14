from django.db import models
from django.contrib.auth.models import User
from guitars.models import Guitar

class Reviews(models.Model):
    """Handles the reviews"""
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    review = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
