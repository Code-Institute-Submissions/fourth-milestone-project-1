from django.shortcuts import render
from .models import OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart
from django.conf import settings

from profiles.models import UserProfile

import stripe


def create_order(request):
    cart = Cart(request)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            if request.user.is_authenticated:
                user_profile = UserProfile.objects.get(user=request.user)
                order.user_profile = user_profile
                order.save()
            cart.clear()
            return render(request, 'orders/order_complete.html', {'order': order})
    else:
        form = CreateOrderForm()
        total = cart.get_total_price()
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        context = {
            'cart': cart,
            'form': form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
    return render(request, 'orders/create_order.html', context)
