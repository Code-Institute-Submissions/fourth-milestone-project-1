from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def shop(request):
    """ Returns the shop products """
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'shop/products.html', context)