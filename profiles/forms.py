from django import forms
from .models import UserProfile


class UserOrderDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)