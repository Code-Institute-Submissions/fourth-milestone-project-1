from django import forms
from .models import UserProfile


class UserOrderDetailsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)
        labels = {
            'default_address_line1': 'Address Line 1',
            'default_address_line2': 'Address Line 2',
            'default_town_or_city': 'Town or City',
            'default_postcode': 'Postcode',
            'default_country': 'Country',
        }
