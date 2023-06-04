from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
import customer.models
from order.models import Order, OrderItem
from product.models import Category
from .forms import RegisterForm
from django.views import View
from .models import Customer
from .forms import ProfileForm
from django.contrib.auth.models import Group

# Create your views here.


class SignupPageView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


class ViewProfile(View):
    @method_decorator(login_required)
    def get(self, request):
        role = request.role
        categories = Category.objects.all()
        customer = Customer.objects.get(username=request.user)
        groups = customer.groups.all()
        group = groups[0].name
        return render(request, 'customer/profile.html', locals())


class ViewListCustomer(View):
    @method_decorator(login_required)
    def get(self, request):
        role = request.role
        categories = Category.objects.all()
        print(request.role)
        if request.role == 'Customer':
            return redirect('/accounts/profile')
        else:
            if request.role == 'Admin':
                list_customer = Customer.objects.all()
                return render(request, 'customer/list_users.html', locals())
            else:
                list_customer = Customer.objects.filter(groups=3)
                return render(request, 'customer/list_users.html', locals())


class ViewProfileByID(View):
    @method_decorator(login_required)
    def get(self, request, pk):
        categories = Category.objects.all()
        role = request.role
        if role == 'Customer':
            return redirect('/accounts/profile')
        else:
            if role == 'Admin':
                customer = get_object_or_404(Customer, pk=pk)
                groups = customer.groups.all()
                group = groups[0].name
                return render(request, 'customer/profile.html', locals())
            else:
                customer = get_object_or_404(Customer, Q(pk=pk) & Q(groups=3))
                groups = customer.groups.all()
                group = groups[0].name
                return render(request, 'customer/profile.html', locals())


class ViewUpdateProfile(View):
    @method_decorator(login_required)
    def get(self, request):
        categories = Category.objects.all()
        role = request.role
        form = ProfileForm(instance=request.user)
        return render(request, 'customer/update_profile.html', locals())


@login_required
def update_profile(request):
    if request.user.has_perm('customer.change_customer'):
        if request.method == 'POST':
            form = ProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                return redirect('profile')
        else:
            form = ProfileForm(instance=request.user)
        return render(request, 'update_profile.html', {'form': form})
    else:
        return HttpResponse('user không có quyền update')


class ViewOrder(View):
    @method_decorator(login_required)
    def get(self,request):
        categories = Category.objects.all()
        role = request.role
        orders = Order.objects.filter(customer=request.user)
        return render(request, 'order/view_order.html', locals())


class ViewOrderDetail(View):
    @method_decorator(login_required)
    def get(self, request, id):
        categories = Category.objects.all()
        role = request.role
        order = Order.objects.get(Q(customer=request.user) & Q(id=id))
        order_item = OrderItem.objects.filter(order=order)
        return render(request, 'order/order_detail.html', locals())