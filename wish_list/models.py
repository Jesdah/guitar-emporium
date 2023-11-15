from django.db import models
from django.contrib.auth.models import User
from guitars.models import Guitar


class WishList(models.Model):
    """Handels Wishlist"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    wishlist_item = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        return self.wishlist_item
