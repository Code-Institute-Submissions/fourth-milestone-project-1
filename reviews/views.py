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
