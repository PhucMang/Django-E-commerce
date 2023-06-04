from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse # new
# Create your models here.


class Category(models.Model):
    title = models.CharField(default='', max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    product_detail = models.TextField(default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    sale_price = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='images/', blank=True)
    inventory = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.title



