# Generated by Django 2.2.7 on 2023-05-19 09:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='active',
        ),
        migrations.RemoveField(
            model_name='product',
            name='active',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='inventory',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='product',
            name='product_detail',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.DeleteModel(
            name='Variation',
        ),
    ]