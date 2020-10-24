from django import forms
from .models import GalleryImage


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = '__all__'
