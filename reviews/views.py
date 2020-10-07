from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ProductReview
from django.contrib.auth.decorators import login_required
from .forms import ProductReviewForm

from shop.models import Product
from profiles.models import UserProfile


@login_required
def create_product_review(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST)
        if form.is_valid():
            review = form.save()
            review.product = product
            user = UserProfile.objects.get(user=request.user)
            review.user = user
            review.save()
            product.calculate_rating()
            return redirect(reverse('product_details', args=[product.id, product.slug]))
    form = ProductReviewForm()
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'reviews/create_product_review.html', context)


@login_required
def edit_product_review(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    user = UserProfile.objects.get(user=request.user)
    review = get_object_or_404(ProductReview, user=user, product=product)
    if request.method == 'POST':
        form = ProductReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            product.calculate_rating()
            return redirect(reverse('product_details',
                            args=[product.id, product.slug]))
    else:
        form = ProductReviewForm(instance=review)
    context = {
        'product': product,
        'form': form,
    }
    return render(request, 'reviews/edit_product_review.html', context)
