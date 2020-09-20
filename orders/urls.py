from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('wh/', webhook, name='webhook'),
]