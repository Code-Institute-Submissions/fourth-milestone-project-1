from django.shortcuts import render
from .models import OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'orders/order_complete.html', {'order': order})
    else:
        form = CreateOrderForm()
        context = {
            'cart': cart,
            'form': form,
            'stripe_public_key': "pk_test_51HTReHJApFJ5JC2dtbCYysmWfbJicF98ZxPtQ5sFsRLsCkD10WQU7soWW7mBOdx2ttR0IIkYYQFtPLnPN1fz5kTr00ERsZXurp",
            'client_secret': 'test',
        }
    return render(request, 'orders/create_order.html', context)
