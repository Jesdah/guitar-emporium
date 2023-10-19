from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from reviews.models import Reviews
from .models import Guitar, Category
from .forms import GuitarForm

# Create your views here.


def all_guitars(request):
    """ A view to show all products, including sorting and search queries """

    guitars = Guitar.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                guitars = guitars.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            guitars = guitars.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            guitars = guitars.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('guitars'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            guitars = guitars.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'guitars': guitars,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'guitars/guitars.html', context)

def guitar_detail(request, guitar_id):
    """ A view to show individual Guitar details and display reviews
    and filter the by guitar_id.
     """

    guitar = get_object_or_404(Guitar, pk=guitar_id)
    reviews = Reviews.objects.filter(guitar=guitar_id)
    context = {
        'guitar': guitar,
        'guitar_reviews': reviews
    }

    return render(request, 'guitars/guitar_detail.html', context)

@login_required
def add_guitar(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GuitarForm(request.POST, request.FILES)
        if form.is_valid():
            guitar = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('guitar_detail', args=[guitar.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = GuitarForm()

    template = 'guitars/add_guitar.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_guitar(request, guitar_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    guitar = get_object_or_404(Guitar, pk=guitar_id)
    if request.method == 'POST':
        form = GuitarForm(request.POST, request.FILES, instance=guitar)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('guitar_detail', args=[guitar.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = GuitarForm(instance=guitar)
        messages.info(request, f'You are editing {guitar.name}')

    template = 'guitars/edit_guitar.html'
    context = {
        'form': form,
        'guitar': guitar,
    }

    return render(request, template, context)


@login_required
def delete_guitar(request, guitar_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    guitar = get_object_or_404(Guitar, pk=guitar_id)
    guitar.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('guitars'))
