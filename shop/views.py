from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.


def shop(request):
    """ Returns the shop products """
    categories = Category.objects.all()
    products = Product.objects.all()
    query = None
    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter a search query.")
                return redirect(reverse('shop'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'categories': categories,
        'products': products,
        'search_text': query,
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