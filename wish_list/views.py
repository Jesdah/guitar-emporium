from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from guitars.models import Guitar
from .models import WishList

@login_required
def add_to_wishlist(request, guitar_id):
    """
    Add to wishlist and if the item is 
    already selected remove from wishlist
    """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, Please login.')
        return redirect(reverse('home'))
    guitar = get_object_or_404(Guitar, pk=guitar_id)
    wishlist_item = WishList.objects.get_or_create(wishlist_item=guitar, user=request.user)
    messages.success(request, 'Guitar added to your wishlist!')

    context = {
        'wishlist_item': wishlist_item,
        'on_profile_page': True,
    }
    return redirect(reverse('guitar_detail', args=[guitar.id]),
     request, 'guitars/guitar_detail.html', context)

@login_required
def remove_from_wishlist(request, guitar_id):

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, Please login.')
        return redirect(reverse('home'))
    guitar = get_object_or_404(Guitar, pk=guitar_id)
    WishList.objects.filter(wishlist_item_id=guitar_id, user_id=request.user).delete()
    messages.success(request, 'Guitar removed from your wishlist!')
    return redirect(reverse('guitar_detail', args=[guitar.id]))
