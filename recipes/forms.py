from django import forms
from .models import Recipe


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('user', 'score', 'is_showcased', 'is_approved', 'saved_by_users')
