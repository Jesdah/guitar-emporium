from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from guitars.models import Guitar
from .models import WishList

def add_to_wishlist(request, guitar_id):
    """
    Add to wishlist and if the item is 
    already selected remove from wishlist
    """
    guitar = get_object_or_404(Guitar, id=guitar_id)
    wishlist_item,created = WishList.objects.get_or_create(wishlist_item=guitar,id=guitar.id,user=request.user,)
    messages.success(request, 'Guitar added to your wishlist!')
    return redirect(reverse('guitar_detail', args=[guitar.id]))

def remove_from_wishlist(request):

    user=request.user
    WishList.objects.filter().delete()
    messages.success(request, 'Guitar removed from your wishlist!')
    return redirect(reverse('guitars'))
