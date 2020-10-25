from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<int:id>/', views.recipe_details, name='recipe_details'),
    path('add-recipe/', views.add_recipe, name='add_recipe'),
    path('<int:id>/edit-recipe/', views.edit_recipe, name='edit_recipe'),
    path('<int:id>/delete-recipe/', views.delete_recipe, name='delete_recipe'),
    path('<int:id>/save-recipe/', views.save_recipe, name='save_recipe'),
    path('<int:id>/remove-recipe/', views.remove_recipe, name='remove_recipe'),
]