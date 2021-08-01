from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'Your shopping cart is currently empty')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IyYoJL6RjrtUtADyEA0Zlg8bh3P7ozp3BQYRsAaf540gdjEelJIEXG6yKum7qxk9xcLFMGeTfxmiGlCVkUpqG05001qBPXBqW',
        'client_secret': 'test_client_secret',
    }

    return render(request, template, context)