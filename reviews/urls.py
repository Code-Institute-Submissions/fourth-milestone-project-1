from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/<slug:slug>/create-review/', views.create_product_review, name='create_product_review'),
]