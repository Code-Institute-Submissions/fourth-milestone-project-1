from django.shortcuts import render, get_object_or_404
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


def product_details(request, id, slug):
    """ Returns the product details page """
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {
        'product': product,
        'categories': categories,
    }

    return render(request, 'shop/product_details.html', context)