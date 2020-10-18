from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['name', 'url', 'is_shown']
    list_filter = ['is_shown']
    list_editable = ['is_shown']
