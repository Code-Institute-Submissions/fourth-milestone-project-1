from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import AddRecipeForm


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


@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save()
            return redirect(reverse('recipe_details', args=[recipe.id]))
    else:
        form = AddRecipeForm()
    context = {
        'form': form,
    }
    return render(request, 'recipes/add_recipe.html', context)
