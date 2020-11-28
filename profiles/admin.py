from django.contrib import admin
from .models import UserProfile
from reviews.admin import ProductReviewInline
from orders.admin import OrderInline


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    inlines = [ProductReviewInline, OrderInline]
    list_display = ['user']
