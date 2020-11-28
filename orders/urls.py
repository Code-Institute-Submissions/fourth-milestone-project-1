from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('checkout/', views.create_order, name='create_order'),
    path('complete/<id>/', views.order_complete, name='order_complete'),
    path('wh/', webhook, name='webhook'),
]
