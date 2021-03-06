from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Recipe
from .forms import AddRecipeForm

from profiles.models import UserProfile


def recipes(request):
    recipes = Recipe.objects.filter(is_approved=True, is_showcased=False)
    showcased_recipes = Recipe.objects.filter(is_approved=True,
                                              is_showcased=True)
    page = request.GET.get('page', 1)
    query = None
    user_profile = None
    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter a search query.")
                return redirect(reverse('recipes'))
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(ingredients__icontains=query) | Q(instructions__icontains=query)
            recipes = recipes.filter(queries)
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
    paginator = Paginator(recipes, 10)
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)
    context = {
        'recipes': recipes,
        'showcased_recipes': showcased_recipes,
        'user_profile': user_profile,
        'search_text': query,
    }
    return render(request, 'recipes/recipes.html', context)


def recipe_details(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if not recipe.is_approved:
        if request.user.is_authenticated:
            user = UserProfile.objects.get(user=request.user)
            if recipe.user == user or request.user.is_superuser:
                context = {
                    'recipe': recipe
                }
                return render(request, 'recipes/recipe_details.html', context)
        return redirect(reverse('recipes'))
    context = {
        'recipe': recipe
    }
    return render(request, 'recipes/recipe_details.html', context)


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            user = UserProfile.objects.get(user=request.user)
            recipe = form.save()
            recipe.user = user
            recipe.save()
            return redirect(reverse('recipe_details', args=[recipe.id]))
    else:
        form = AddRecipeForm()
    context = {
        'form': form,
    }
    return render(request, 'recipes/add_recipe.html', context)


@login_required
def edit_recipe(request, id):
    user = UserProfile.objects.get(user=request.user)
    recipe = get_object_or_404(Recipe, id=id, user=user)
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            recipe.user = user
            recipe.save()
            return redirect(reverse('recipe_details', args=[recipe.id]))
    else:
        form = AddRecipeForm(instance=recipe)
    context = {
        'recipe': recipe,
        'form': form,
    }
    return render(request, 'recipes/edit_recipe.html', context)


@login_required
def delete_recipe(request, id):
    user = UserProfile.objects.get(user=request.user)
    recipe = get_object_or_404(Recipe, id=id, user=user)
    recipe.delete()
    return redirect(reverse('recipes'))


@login_required
@require_POST
def save_recipe(request, id):
    user = UserProfile.objects.get(user=request.user)
    recipe = get_object_or_404(Recipe, id=id)
    recipe.saved_by_users.add(user)
    recipe.score += 1
    recipe.save()
    redirect_path = request.POST.get('redirect_path')
    return redirect(redirect_path)


@login_required
@require_POST
def remove_recipe(request, id):
    user = UserProfile.objects.get(user=request.user)
    recipe = get_object_or_404(Recipe, id=id)
    recipe.saved_by_users.remove(user)
    recipe.score -= 1
    recipe.save()
    redirect_path = request.POST.get('redirect_path')
    return redirect(redirect_path)
