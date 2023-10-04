from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from guitars.models import Guitar

def cart_contents(request):

    cart_items = []
    total = 0
    guitar_count = 0
    cart = request.session.get('cart', {})

    for item_id, item_data in cart.items():
        if isinstance(item_data, int):
            guitar = get_object_or_404(Guitar, pk=item_id)
            total += item_data * guitar.price
            guitar_count += item_data
            cart_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'guitar': guitar,
            })
        # else:
        #     guitar = get_object_or_404(Guitar, pk=item_id)
        #     for size, quantity in item_data['items_by_size'].items():
        #         total += quantity * guitar.price
        #         guitar_count += quantity
        #         cart_items.append({
        #             'item_id': item_id,
        #             'quantity': quantity,
        #             'guitar': guitar,
        #             'size': size,
        #         })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'guitar_count': guitar_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'grand_total': grand_total,
    }

    return context
