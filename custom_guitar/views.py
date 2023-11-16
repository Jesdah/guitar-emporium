from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .models import Custom
from .forms import CustomGuitarForm


def submit_custom_guitar_form(request):
    """ Renders the custom guitar form """

    custom_guitar = Custom.objects.all()
    if request.method == 'POST':
        form = CustomGuitarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have submitted your application, '
                             'our workshop will contact you '
                             'as soon as possible!')
            return redirect(reverse('guitars'))
        else:
            messages.error(request,
                           'Failed to submit the form.'
                           ' Please ensure the form is valid.')
    else:
        form = CustomGuitarForm()

    template = 'custom/custom.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
