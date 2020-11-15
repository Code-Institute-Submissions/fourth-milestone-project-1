from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import UserProfile
from .forms import UserOrderDetailsForm

from recipes.models import Recipe


@login_required
def user_profile(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    form = UserOrderDetailsForm(instance=user_profile)
    orders = user_profile.orders.all()
    context = {
        'user_profile': user_profile,
        'form': form,
        'orders': orders,
    }
    return render(request, 'profiles/profile.html', context)


@login_required
def website_admin(request):
    if not request.user.is_superuser:
        return redirect(reverse('home'))
    else:
        unapproved_recipes = Recipe.objects.filter(is_approved=False)
        page = request.GET.get('page', 1)
        paginator = Paginator(unapproved_recipes, 5)
        try:
            unapproved_recipes = paginator.page(page)
        except PageNotAnInteger:
            unapproved_recipes = paginator.page(1)
        except EmptyPage:
            unapproved_recipes = paginator.page(paginator.num_pages)
        context = {
            'unapproved_recipes': unapproved_recipes,
        }
        return render(request, 'profiles/website_admin.html', context)


@login_required
def user_recipes(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_recipes = Recipe.objects.filter(user=user_profile)
    paginator = Paginator(user_recipes, 10)
    page = request.GET.get('page', 1)
    try:
        user_recipes = paginator.page(page)
    except PageNotAnInteger:
        user_recipes = paginator.page(1)
    except EmptyPage:
        user_recipes = paginator.page(paginator.num_pages)
    context = {
        'user_profile': user_profile,
        'user_recipes': user_recipes,
    }
    return render(request, 'profiles/user_recipes.html', context)


@login_required
def saved_recipes(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    saved_recipes = Recipe.objects.filter(saved_by_users=user_profile, is_approved=True)
    paginator = Paginator(saved_recipes, 10)
    page = request.GET.get('page', 1)
    try:
        saved_recipes = paginator.page(page)
    except PageNotAnInteger:
        saved_recipes = paginator.page(1)
    except EmptyPage:
        saved_recipes = paginator.page(paginator.num_pages)
    context = {
        'user_profile': user_profile,
        'saved_recipes': saved_recipes,
    }
    return render(request, 'profiles/saved_recipes.html', context)
