from django.contrib import admin
from .models import ProductReview


class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    raw_id_fields = ['product', 'user']


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'rating']