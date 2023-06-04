from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, Http404, redirect, HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from cart.models import Cart, CartItem ,Product
from . import forms
from .models import Order, OrderItem
from customer.models import Customer
from product.models import Category

# Create your views here.


class Checkout(View):
    @method_decorator(login_required)
    def get(self, request):
        role = request.role
        user = request.user
        categories = Category.objects.all()
        customer = Customer.objects.get(username=user)
        carts = Cart.objects.filter(customer=user)
        if carts:
            cart = Cart.objects.get(customer=user)
            form = forms.FormCheckout()
            cart_item = CartItem.objects.filter(cart=cart)
            amount = 0
            for i in cart_item:
                value = i.quantity * i.item.sale_price
                amount = amount + value
            total_amount = amount + 10000
            return render(request, 'order/checkout.html', locals())
        else:
            Cart(customer=user).save()
            form = forms.FormCheckout()
            return render(request, 'order/checkout.html', locals())


@login_required
def add_order(request):
    if request.method == "POST":
        role = request.role
        categories = Category.objects.all()
        user = request.user
        cart = Cart.objects.get(customer=user)
        cart_items = CartItem.objects.filter(cart=cart)
        amount = 0
        for i in cart_items:
            value = i.quantity * i.item.sale_price
            amount = amount + value
        total_amount = amount + 10000
        form = forms.FormCheckout(request.POST)
        if form.is_valid():
            shipping_address = form.cleaned_data['shipping_address']
            order_description = form.cleaned_data['order_description']
            Order(customer=user, shipping_address=shipping_address,
                  order_description=order_description,
                  amount=amount, total_amount=total_amount).save()
            orders = Order.objects.filter(customer=user).order_by('-id').first()
            order_id = orders.id
            order = Order.objects.get(Q(customer=user) & Q(id=order_id))
            for cart_item in cart_items:
                p = cart_item.item
                q = cart_item.quantity
                OrderItem(order=order, item=p, quantity=q).save()
            cart.delete()
            order_item = OrderItem.objects.filter(order=order)

            return render(request, 'order/checkout_complete.html', locals())
        else:
            return redirect('/checkout')
    else:
        return HttpResponse('request method not POST')




