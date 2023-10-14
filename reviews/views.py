from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import ReviewsForm
from .models import Reviews, User
from guitars.models import Guitar

def add_review(request, guitar_id):
    """ A view to return the review page """

    queryset = Guitar.objects.filter()
    guitar = get_object_or_404(queryset, id=guitar_id)
    # reviews = guitar.reviews.filter()
    review = Reviews.guitar
    review_form = ReviewsForm(request.POST)
    # user = get_object_or_404(User, id=user_id)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.guitar = guitar
        review.save()
        messages.success(request, 'New Destination created')
    else:
        messages.error(request, 'Something went wrong!')
    template = 'reviews/review.html'
    context = {
        'form': review_form,
        'guitar': guitar
        # 'user': user,
    }

    return render(request, template, context)
