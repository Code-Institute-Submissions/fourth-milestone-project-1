from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Order, OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart
from django.conf import settings

from profiles.models import UserProfile
from profiles.forms import UserOrderDetailsForm

import stripe


# Order process based on Boutique Ado course content
def create_order(request):
    cart = Cart(request)
    if not cart:
        return redirect('view_cart')
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                quantity = item['quantity']
                product = item['product']
                OrderItem.objects.create(order=order,
                                         product=product,
                                         price=item['price'],
                                         quantity=quantity)
                product.stock -= quantity
                product.save()
            if request.user.is_authenticated:
                user_profile = UserProfile.objects.get(user=request.user)
                order.user_profile = user_profile
                order.save()
                update_default = 'update-default' in request.POST
                if update_default:
                    new_default = {
                        'default_address_line1': order.address_line1,
                        'default_address_line2': order.address_line2,
                        'default_town_or_city': order.town_or_city,
                        'default_postcode': order.postcode,
                        'default_country': order.country,
                    }
                    form = UserOrderDetailsForm(new_default,
                                                instance=user_profile)
                    if form.is_valid():
                        form.save()
            cart.clear()
            return redirect(reverse('order_complete', args=[order.id]))
    else:
        total = cart.get_total_price()
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        if request.user.is_authenticated:
            try:
                user_profile = UserProfile.objects.get(user=request.user)
                form = CreateOrderForm(initial={
                    'email': user_profile.user.email,
                    'address_line1': user_profile.default_address_line1,
                    'address_line2': user_profile.default_address_line2,
                    'town_or_city': user_profile.default_town_or_city,
                    'postcode': user_profile.default_postcode,
                    'country': user_profile.default_country,
                })
            except UserProfile.DoesNotExist:
                form = CreateOrderForm()
        else:
            form = CreateOrderForm()
        context = {
            'cart': cart,
            'form': form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
    return render(request, 'orders/create_order.html', context)


def order_complete(request, id):
    order = get_object_or_404(Order, id=id)
    context = {
        'order': order,
    }
    return render(request, 'orders/order_complete.html', context)
