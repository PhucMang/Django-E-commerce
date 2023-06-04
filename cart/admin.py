from django.contrib import admin
from .models import Cart, CartItem
# Register your models here.


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'total',
        'created_at',
        'updated_at',
    ]
    list_filter = [
        'customer',
        'total',
        'created_at',
        'updated_at',
    ]
    search_fields = [
        'id',
        'customer',
        'total',
    ]


@admin.register(CartItem)
class CartItemModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'cart',
        'item',
        'created_at',
        'updated_at',
    ]
    list_filter = [
        'cart',
        'item',
    ]
    search_fields = [
        'id',
        'cart',
        'item',
    ]