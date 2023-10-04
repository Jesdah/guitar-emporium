from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from guitars.models import Guitar

# Create your views here.

def view_cart(request):
    """ A view that renders the bag contents page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    guitar = get_object_or_404(Guitar, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    # if size:
    #     if item_id in list(bag.keys()):
    #         if size in bag[item_id]['items_by_size'].keys():
    #             bag[item_id]['items_by_size'][size] += quantity
    #             messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
    #         else:
    #             bag[item_id]['items_by_size'][size] = quantity
    #             messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    #     else:
    #         bag[item_id] = {'items_by_size': {size: quantity}}
    #         messages.success(request, f'Added size {size.upper()} {product.name} to your bag')
    # else:
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {guitar.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {guitar.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    guitar = get_object_or_404(Guitar, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})

    # if size:
    #     if quantity > 0:
    #         bag[item_id]['items_by_size'][size] = quantity
    #         messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
    #     else:
    #         del bag[item_id]['items_by_size'][size]
    #         if not bag[item_id]['items_by_size']:
    #             bag.pop(item_id)
    #         messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    # else:
    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {guitar.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {guitar.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        guitar = get_object_or_404(Guitar, pk=item_id)
        # size = None
        # if 'product_size' in request.POST:
        #     size = request.POST['product_size']
        cart = request.session.get('cart', {})

        # if size:
        #     del bag[item_id]['items_by_size'][size]
        #     if not bag[item_id]['items_by_size']:
        #         bag.pop(item_id)
        #     messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
        if cart.pop(item_id):
            messages.success(request, f'Removed {guitar.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)