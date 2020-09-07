from django.shortcuts import render
from .models import Product

# Create your views here.


def shop(request):
    """ Returns the shop products """
    products = Product.objects.all()

    context = {
        'products' : products,
    }

    return render(request, 'shop/products.html', context)