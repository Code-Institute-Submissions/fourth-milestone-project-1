from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('add-image/', views.add_image, name='add_image'),
    path('<int:id>/edit-image/', views.edit_image, name='edit_image'),
]
