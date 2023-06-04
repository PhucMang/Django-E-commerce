from django.contrib import admin
from .models import Customer
from .views import ViewListCustomer
# Register your models here.


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'username',
        'email',
    ]
    search_fields = [
        'id',
        'username',
        'email',
    ]


