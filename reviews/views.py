from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import ReviewsForm
from .models import Reviews
from guitars.models import Guitar
from profiles.models import UserProfile

def add_review(request, guitar_id):
    """ A view to return the review page """
    profile = get_object_or_404(UserProfile, user=request.user)
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
        messages.success(request, 'Your review has been submited!')
        return redirect(reverse('guitar_detail', args=[guitar.id]))

    template = 'reviews/review.html'
    context = {
        'form': review_form,
        'guitar': guitar,
        'profile': profile,
    }

    return render(request, template, context)


def view_review(request, guitar_id):

    queryset = Reviews.objects.filter()
    guitar_reviews = get_object_or_404(queryset, id=guitar_id)
    reviews = guitar_reviews.guitar.filter().order_by('post_date')

    context = {
        'reviews': reviews
    }

    return render(request, 'guitars/templates/guitars/guitar_detail.html', context)
