

def cart_info(request):

    cart_items = []
    total_cost = 0
    product_count = 0

    context = {
        'cart_items': cart_items,
        'total_cost': total_cost,
        'product_count': product_count,
    }

    return context
