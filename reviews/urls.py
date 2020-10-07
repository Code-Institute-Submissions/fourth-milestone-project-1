from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/<slug:slug>/create-review/', views.create_product_review, name='create_product_review'),
    path('<int:id>/<slug:slug>/edit-review/', views.edit_product_review, name='edit_product_review'),
]