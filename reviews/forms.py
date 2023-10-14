from django import forms
from .models import Reviews

class ReviewsForm(forms.ModelForm):
    """
    Reviews form.
    """
    class Meta:
        model = Reviews
        fields = ('review',)
