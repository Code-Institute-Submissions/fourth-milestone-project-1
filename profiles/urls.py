from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('website-admin/', views.website_admin, name='website_admin'),
    path('recipes/', views.profile_recipes, name='profile_recipes'),
]