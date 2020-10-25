from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required

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
        return render(request, 'profiles/website_admin.html')


@login_required
def profile_recipes(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    user_recipes = Recipe.objects.filter(user=user_profile)
    saved_recipes = Recipe.objects.filter(saved_by_users=user_profile)
    context = {
        'user_profile': user_profile,
        'user_recipes': user_recipes,
        'saved_recipes': saved_recipes,
    }
    return render(request, 'profiles/profile_recipes.html', context)
