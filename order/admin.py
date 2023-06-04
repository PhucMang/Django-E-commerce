from django.contrib import admin
from .models import Order,OrderItem
# Register your models here.


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'amount',
        'total_amount',
        'shipping_address',
        'created_at',
        'updated_at',
        'is_completed',
    ]
    list_filter = [
        'customer',
        'amount',
        'total_amount',
        'created_at',
        'updated_at',
    ]
    search_fields = [
        'id',
        'customer',
        'total',
    ]

@admin.register(OrderItem)
class OrderItemModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'order',
        'item',
        'quantity',
        'created_at',
        'updated_at',
    ]
    list_filter = [
        'order',
        'item',
    ]
    search_fields = [
        'id',
        'order',
        'item',
    ]