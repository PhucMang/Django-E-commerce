from django.shortcuts import render
from django.views import View
from product.models import Category, Product
# Create your views here.


class HomeView(View):
    def get(self, request):
        role = None
        if request.role:
            role = request.role
        categories = Category.objects.all()
        products = Product.objects.all()
        last_eight_products = Product.objects.all().order_by('-id')[:8]
        return render(request, 'homepage/index.html', locals())


