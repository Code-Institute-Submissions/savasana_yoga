from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib import messages

from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    # Creates a new dictionary so items can be removed
    new_cart = {k: v for k, v in cart.items()}

    # loops over new dictionary and checks if product exists
    for item_id, quantity in new_cart.items():
        product_id = item_id
        try:
            product = Product.objects.get(pk=product_id)
            # delete product from cart if no longer in database
        except Product.DoesNotExist:
            del cart[item_id]
            messages.error(request, 'This product is no longer available')
            continue

        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,

        })

    request.session['cart'] = cart
    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
