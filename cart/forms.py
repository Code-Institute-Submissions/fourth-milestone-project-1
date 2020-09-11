from django import forms

QUANTITY_RANGE = [(i, str(i)) for i in range(1, 11)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=QUANTITY_RANGE, coerce=int)
    overwrite = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
