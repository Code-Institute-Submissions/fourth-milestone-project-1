from django.urls import path
from . import views

urlpatterns = [
    path('', views.videos, name='videos'),
    path('add-video/', views.add_video, name='add_video'),
]
