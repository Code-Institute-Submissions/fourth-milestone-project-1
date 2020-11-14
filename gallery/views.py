from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import GalleryImage
from .forms import UploadImageForm

from shop.models import Product


def gallery(request):
    products = Product.objects.exclude(image1__exact='')
    images = GalleryImage.objects.filter(is_shown=True)
    paginator = Paginator(products, 48)
    page = request.GET.get('page1')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    paginator = Paginator(images, 48)
    page = request.GET.get('page2')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    context = {
        'products': products,
        'images': images

    }
    return render(request, 'gallery/gallery.html', context)


@login_required
def add_image(request):
    if not request.user.is_superuser:
        return redirect(reverse('gallery'))
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('gallery'))
    else:
        form = UploadImageForm()
    context = {
        'form': form,
    }
    return render(request, 'gallery/add_image.html', context)


@login_required
def edit_image(request, id):
    if not request.user.is_superuser:
        return redirect(reverse('gallery'))
    image = get_object_or_404(GalleryImage, id=id)
    if request.method == 'POST':
        form = UploadImageForm(request.POST, instance=image)
        if form.is_valid():
            form.save()
            return redirect(reverse('gallery'))
    else:
        form = UploadImageForm(instance=image)
    context = {
        'form': form,
        'image': image,
    }
    return render(request, 'gallery/edit_image.html', context)


@login_required
def delete_image(request, id):
    if not request.user.is_superuser:
        return redirect(reverse('gallery'))
    image = get_object_or_404(GalleryImage, id=id)
    image.delete()
    return redirect(reverse('gallery'))
