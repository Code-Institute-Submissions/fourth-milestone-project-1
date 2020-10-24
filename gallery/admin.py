from django.contrib import admin
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'is_shown']
    list_filter = ['is_shown']
    list_editable = ['is_shown']
