from django.shortcuts import render
from shop.models import Product, Category

# Create your views here.

def view_cart(request):
    """View to return the shopping cart"""
    categories = Category.objects.all()
    context = {
        'categories': categories,

    }
    return render(request, 'cart/cart.html', context)
