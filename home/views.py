from django.shortcuts import render
from shop.models import Category

# Create your views here.


def index(request):
    """ Returns the index page """
    categories = Category.objects.all()
    context = {
        'categories': categories

    }
    return render(request, 'home/index.html', context)
