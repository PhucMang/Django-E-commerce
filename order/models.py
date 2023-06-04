from django.core.validators import MinValueValidator
from django.db import models
from customer.models import Customer
from cart.models import Cart, Product
# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=255, default='')
    order_description = models.TextField(default='')
    amount = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    total_amount = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pk.__str__()


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pk.__str__()