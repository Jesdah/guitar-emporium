from django.shortcuts import render

def custom_guitar(request):
    """ A view to return the contact form page."""

    return render(request, 'custom/custom.html')
