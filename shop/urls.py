from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop'),
    path('<int:id>/<slug:slug>/', views.product_details, name='product_details')
]
