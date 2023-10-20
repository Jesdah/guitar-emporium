from django.shortcuts import render
from django.contrib import messages

from guitars.models import Guitar
from .models import WishList

def add_to_wishlist(request, guitar_id):
    """
    Add to wishlist and if the item is 
    already selected remove from wishlist
    """
    item = Guitar.objects.get(id=guitar_id)
    obj, created = WishList.objects.get_or_create(user=request.user)
    if item in obj.wishlist_item.all():
        obj.wishlist_item.remove(item)
        return messages.success(request, 'Item has been removed from wishlist!')
    else:
        obj.wishlist_item.add(item)
        return messages.success(request, 'Item has been added to wishlist!')
