from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'score', 'is_approved', 'is_showcased']
    list_filter = ['is_approved', 'is_showcased']
    list_editable = ['is_approved', 'is_showcased']
