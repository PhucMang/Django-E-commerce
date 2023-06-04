from django.urls import path
from . import views

urlpatterns = [
    path('', views.Checkout.as_view(), name='checkout'),
    path('checkout-complete/', views.add_order, name='add-order'),
]