from django.shortcuts import render

from shop.models import Product


def gallery(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'gallery/gallery.html', context)
