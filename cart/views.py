from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product, Category
from .cart import Cart
from .forms import CartAddProductForm

# Create your views here.

def view_cart(request):
    """View to return the shopping cart"""
    categories = Category.objects.all()
    context = {
        'categories': categories,

    }
    return render(request, 'cart/cart.html', context)

@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], overwrite_quantity=cd['overwrite'])
    redirect_path = request.POST.get('redirect_path')
    return redirect(redirect_path)
