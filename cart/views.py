from django.db.models import Q
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views import View
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required, permission_required
from product.models import Product, Category
from .models import Cart, CartItem
from django.http import JsonResponse

# Create your views here.


class ViewCart(View):
    @method_decorator(login_required, permission_required(perm='cart.view_cart'))
    def get(self, request):
        categories = Category.objects.all()
        user = request.user
        role = request.role
        cart = Cart.objects.filter(customer=user)
        if cart:
            cart = Cart.objects.get(customer=user)
            cart_item = CartItem.objects.filter(cart=cart)
            amount = 0
            for i in cart_item:
                value = i.quantity * i.item.sale_price
                amount = amount + value
            total_amount = amount + 10000
            cart.total = total_amount
            cart.save()
            return render(request, 'cart/cart.html', locals())
        else:
            Cart(customer=user).save()
            return render(request, 'cart/cart.html', locals())


@login_required
@permission_required(perm=['cart.add_cart',
                           'cart.add_cartitem',
                           ])
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('product_id')
    carts = Cart.objects.filter(customer=user)
    if carts:
        cart = Cart.objects.get(customer=user)
        product = Product.objects.get(id=product_id)
        cart_item = CartItem.objects.filter(Q(item=product) & Q(cart=cart))
        if cart_item:
            return redirect("/cart")
        else:
            CartItem(cart=cart, item=product).save()
            return redirect("/cart")
    else:
        Cart(customer=user).save()
        cart = Cart.objects.get(customer=user)
        product = Product.objects.get(id=product_id)
        CartItem(cart=cart, item=product).save()
        return redirect("/cart")


def plus_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        user = request.user
        cart = Cart.objects.get(customer=user)
        c = CartItem.objects.get(Q(item=product_id) & Q(cart=cart))
        c.quantity += 1
        c.save()
        cart_item = CartItem.objects.filter(cart=cart)
        amount = 0
        for i in cart_item:
            value = i.quantity * i.item.sale_price
            amount = amount + value
        total_amount = amount + 10000
        cart.total = total_amount
        cart.save()
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount,
        }
        return JsonResponse(data)


def minus_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        user = request.user
        cart = Cart.objects.get(customer=user)
        c = CartItem.objects.get(Q(item=product_id) & Q(cart=cart))
        c.quantity -= 1
        c.save()
        if c.quantity <= 0:
            c.delete()
        cart_item = CartItem.objects.filter(cart=cart)
        amount = 0
        for i in cart_item:
            value = i.quantity * i.item.sale_price
            amount = amount + value
        total_amount = amount + 10000
        cart.total = total_amount
        cart.save()
        data = {
            'quantity': c.quantity,
            'amount': amount,
            'total_amount': total_amount,
        }
        return JsonResponse(data)


def remove_cart(request):
    if request.method == 'GET':
        product_id = request.GET['product_id']
        cart = Cart.objects.get(customer=request.user)
        c = CartItem.objects.get(Q(item=product_id) & Q(cart=cart))
        c.delete()
        # user = request.user
        cart_item = CartItem.objects.filter(cart=cart)
        amount = 0
        for i in cart_item:
            value = i.quantity * i.item.sale_price
            amount = amount + value
        total_amount = amount + 10000
        data = {
            'amount': amount,
            'total_amount': total_amount,
        }
        return JsonResponse(data)
