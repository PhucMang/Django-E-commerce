from django.urls import path
from . import views
urlpatterns = [
    path('', views.ViewCart.as_view(), name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('pluscart/', views.plus_cart, name='plus-cart'),
    path('minuscart/', views.minus_cart, name='minus-cart'),
    path('removecart/',views.remove_cart, name='remove-cart'),
]