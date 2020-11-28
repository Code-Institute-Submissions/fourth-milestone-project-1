from django.contrib import admin
from .models import Category, Product
from reviews.admin import ProductReviewInline


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'friendly_name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductReviewInline]
    list_display = ['name', 'price', 'available',
                    'stock', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'stock']
    prepopulated_fields = {'slug': ('name',)}
