from django.core.validators import MinValueValidator
from django.db import models
from product.models import Product
from customer.models import Customer
# Create your models here.


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.__str__()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pk.__str__()

    @property
    def total_cost(self):
        return self.quantity * self.item.sale_price