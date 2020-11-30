from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


# Cart functionality largely taken from Chapter 7 of book
# "Django 3 By Example" by Antonio Melé
def view_cart(request):
    """View to return the shopping cart"""
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'], 'overwrite': True})
    context = {
        'cart': cart,
    }
    return render(request, 'cart/cart.html', context)


# Cart functionality largely taken from Chapter 7 of book
# "Django 3 By Example" by Antonio Melé
@require_POST
def add_to_cart(request, product_id):
    """View to add product and quantity to the cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                 overwrite_quantity=cd['overwrite'])
    redirect_path = request.POST.get('redirect_path')
    return redirect(redirect_path)


@require_POST
def remove_from_cart(request, product_id):
    """View to remove product from the cart"""
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('view_cart')
