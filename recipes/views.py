from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Recipe


def recipes(request):
    recipes = Recipe.objects.all()
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
