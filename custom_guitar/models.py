from django.db import models

class Custom(models.Model):
    """
    A model for customers who want to book a consultation
     to buy a custom-designed guitar.
    """

    title=models.CharField(max_length=50, null=False, blank=False)
    full_name=models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField(null=False, blank=False)
    phone_number=models.CharField(max_length=20)
    message=models.CharField(max_length=1000, null=False, blank=False)
    make_contact=models.DateField()
