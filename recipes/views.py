from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Recipe
from .forms import AddRecipeForm

from profiles.models import UserProfile


def recipes(request):
    recipes = Recipe.objects.all()
    query = None
    if request.GET:
        if 'search' in request.GET:
            query = request.GET['search']
            if not query:
                messages.error(request, "Please enter a search query.")
                return redirect(reverse('recipes'))
            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(ingredients__icontains=query) | Q(instructions__icontains=query)
            recipes = recipes.filter(queries)
    context = {
        'recipes': recipes
    }
    return render(request, 'recipes/recipes.html', context)


def recipe_details(request, id):
    recipe = get_object_or_404(Recipe, id=id)
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
