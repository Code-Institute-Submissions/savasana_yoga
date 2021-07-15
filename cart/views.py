from django.shortcuts import render, redirect

# Create your views here.


def view_cart(request):
    """ A view that renders the cart contents page """

    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ A view to add quantity of an item to the shopping cart 
        Submits form to this view incl quantity and item_id
        Creates cart variable if it doesn't exist, or gets it from the session, 
        Either adds the item to the cart, if it doesn't exist, or updates the quantity if it already exists,
        Finally overwrites the cart variable with the new updated cart
    """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
