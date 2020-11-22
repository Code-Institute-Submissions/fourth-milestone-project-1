from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('orders/', views.user_orders, name='user_orders'),
    path('website-admin/', views.website_admin, name='website_admin'),
    path('my-recipes/', views.user_recipes, name='user_recipes'),
    path('saved-recipes/', views.saved_recipes, name='saved_recipes'),
]
