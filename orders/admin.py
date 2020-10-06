from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderInline(admin.TabularInline):
    model = Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address_line1', 'postcode', 'town_or_city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
