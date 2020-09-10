from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product, Category

# Create your views here.

def view_cart(request):
    """View to return the shopping cart"""
    categories = Category.objects.all()
    context = {
        'categories': categories,

    }
    return render(request, 'cart/cart.html', context)


def add_to_cart(request, product_id):
    """ Add product to cart with correct quantity and spec"""
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity'))
    redirect_path = request.POST.get('redirect_path')
    cart = request.session.get('cart', {})
    if product_id in list(cart.keys()):
        cart[product_id]['quantity'] += quantity
    else:
        cart[product_id] = {'quantity': quantity,
                            'price': str(product.price)}
    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_path)
