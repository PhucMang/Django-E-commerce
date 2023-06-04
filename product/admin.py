from django.contrib import admin
from .models import Product, Category
# Register your models here.


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'price',
        'sale_price',
        'category',
        'image',
    ]
    list_filter = [
        'category',
        'price',
        'sale_price',

    ]
    search_fields = [
        'id',
        'title',
        'category',
    ]


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'description',
        'image',
    ]
    search_fields = [
        'id',
        'title',
    ]