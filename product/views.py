from django.db.models import Q
from django.shortcuts import render, get_object_or_404, Http404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Product, Category
from .forms import ProductSearchForm

# Create your views here.


class ViewListProduct(View):
    def get(self, request):
        role = request.role
        categories = Category.objects.all()
        product = Product.objects.all().order_by('-id')
        return render(request, 'product/shop.html', locals())


class ProductDetail(View):
    def get(self, request, pk):
        role = request.role
        product = get_object_or_404(Product, pk=pk)
        categories = Category.objects.all()
        return render(request, 'product/product_detail.html', locals())


class ViewCategory(View):
    def get(self,request, category_slug=None):
        role = request.role
        product = Product.objects.all().order_by('-id')
        categories = Category.objects.all()
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            product = product.filter(category=category)
            return render(request, 'product/category.html', locals())


def search_product(request):
    role = request.role
    categories = Category.objects.all()
    search = request.GET.get('search')
    product = Product.objects.filter(title__icontains=search)
    return render(request, 'product/product_search.html', locals())

