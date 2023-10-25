from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from guitars.models import Guitar
from .forms import ReviewsForm
from .models import Reviews



@login_required
def add_review(request, guitar_id):
    """ A view to return the review page """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, Please login.')
        return redirect(reverse('home'))
    queryset = Guitar.objects.filter()
    guitar = get_object_or_404(queryset, id=guitar_id)

    review = Reviews.guitar
    review_form = ReviewsForm(request.POST)

    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.guitar = guitar
        review.author = request.user.username
        review.save()
        messages.success(request, 'Your review has been submited!')
        return redirect(reverse('guitar_detail', args=[guitar.id]))

    template = 'reviews/review.html'
    context = {
        'form': review_form,
        'guitar': guitar,
    }

    return render(request, template, context)

