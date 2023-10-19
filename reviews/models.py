from django.db import models
from guitars.models import Guitar


class Reviews(models.Model):
    """Handles the reviews"""
    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)
    author = models.CharField(max_length=80)
    review = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Order by post date.
        """
        ordering = ["post_date"]

    def __str__(self):
        return self.review
