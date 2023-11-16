from django import forms
from .models import Custom


class DateInput(forms.DateInput):
    """
    I am using this to get a datepicker.
    """
    input_type = 'date'


class CustomGuitarForm(forms.ModelForm):

    class Meta:
        model = Custom
        fields = ('title',
                  'full_name',
                  'email',
                  'phone_number',
                  'message',
                  'make_contact',)

        widgets = {'make_contact': DateInput(), }

        labels = {
            'make_contact': (
                'Tell us what day you want us'
                ' to contact you for a consultation.'
                ), }
