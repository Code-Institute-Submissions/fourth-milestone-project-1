from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:id>/<slug:slug>/', views.product_details, name='product_details'),
    path('add-product/', views.add_new_product, name='add_product'),
    path('<int:id>/<slug:slug>/edit-product/', views.edit_product, name='edit_product'),
    path('<int:id>/<slug:slug>/delete-product/', views.delete_product, name='delete_product'),
]
