from django.conf import settings
from decimal import Decimal
from shop.models import Product


# Cart functionality largely taken from Chapter 7 of book
# "Django 3 By Example" by Antonio Melé
class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, overwrite_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if overwrite_quantity:
            self.cart[product_id]['quantity'] = quantity
            cart_quantity = self.cart[product_id]['quantity']
            stock = product.stock
            if cart_quantity > stock:
                self.cart[product_id]['quantity'] = stock
        else:
            self.cart[product_id]['quantity'] += quantity
            cart_quantity = self.cart[product_id]['quantity']
            stock = product.stock
            if cart_quantity > stock:
                self.cart[product_id]['quantity'] = stock
                cart_quantity = self.cart[product_id]['quantity']
            if cart_quantity > 10:
                self.cart[product_id]['quantity'] = 10
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
        self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity']
                   for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
