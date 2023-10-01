from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

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
