from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category
from .forms import ProductForm
from cart.forms import CartAddProductForm

from reviews.models import ProductReview

# Create your views here.


def shop(request):
    """ Returns the shop products """
    categories = Category.objects.all()
    products = Product.objects.all()
    query = None
    filter_categories = None
    if request.GET:
        if 'category' in request.GET:
            filter_categories = request.GET['category'].split(',')
            products = products.filter(category__slug__in=filter_categories)
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
        'filter_categories': filter_categories,
    }
    return render(request, 'shop/products.html', context)


def product_details(request, id, slug):
    """ Returns the product details page """
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    reviews = product.product_reviews.all()
    context = {
        'product': product,
        'categories': categories,
        'cart_product_form': cart_product_form,
        'reviews': reviews,
    }
    return render(request, 'shop/product_details.html', context)


@login_required
def add_new_product(request):
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect(reverse('product_details', args=[product.id, product.slug]))
    else:
        form = ProductForm()
    context = {
        'form': form,
    }
    return render(request, 'shop/add_product.html', context)


@login_required
def edit_product(request, id, slug):
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    product = get_object_or_404(Product, id=id, slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('product_details',
                            args=[product.id, product.slug]))
    else:
        form = ProductForm(instance=product)
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'shop/edit_product.html', context)


@login_required
def delete_product(request, id, slug):
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    product = get_object_or_404(Product, id=id, slug=slug)
    product.delete()
    return redirect(reverse('shop'))
