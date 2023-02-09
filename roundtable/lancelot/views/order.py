"""订单详情页"""
from django.forms import inlineformset_factory
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.views import View

from lancelot.decorators import allowed_users
from lancelot.filters import OrderFilter
from lancelot.forms import CustomerForm
from lancelot.models import Customer, Order, Product


class AccountSettings(View):
    """用户修改用户名并存入customer"""

    @method_decorator(allowed_users(allowed_roles=['customer']))
    def get(self, request):
        customer = request.user.customer
        form = CustomerForm(instance=customer)

        context = {'form': form}
        return render(request, 'lancelot/account_settings.html', context)

    @method_decorator(allowed_users(allowed_roles=['customer']))
    def post(self, request):
        customer = request.user.customer
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

        context = {'form': form}
        return render(request, 'lancelot/account_settings.html', context)


class ProductsPage(View):
    """查看所有商品"""

    def get(self, request):
        products = Product.objects.all()

        context = {'products': products}
        return render(request, 'lancelot/products.html', context)


class CustomerPage(View):
    """根据用户id查找其订单信息"""

    # @method_decorator(allowed_users(allowed_roles=['admin']))
    def get(self, request, pk):
        customer = Customer.objects.get(id=pk)

        orders = customer.order_set.all()
        order_count = orders.count()

        myFilter = OrderFilter(request.GET, queryset=orders)
        orders = myFilter.qs

        context = {
            'customer': customer,
            'orders': orders,
            'order_count': order_count,
            'myFilter': myFilter
        }
        return render(request, 'lancelot/customer.html', context)


class OrderPage(View):

    def get(self, request, pk):
        OrderFormSet = inlineformset_factory(
            Customer, Order,
            fields=('product', 'status'), extra=10
        )
        customer = Customer.objects.get(id=pk)
        formset = OrderFormSet(
            queryset=Order.objects.none(),
            instance=customer
        )

        context = {'form': formset}
        return render(request, 'lancelot/order_form.html', context)

    # @method_decorator(allowed_users(allowed_roles=['admin']))
    def post(self, request, pk):
        OrderFormSet = inlineformset_factory(
            Customer, Order,
            fields=('product', 'status'), extra=10
        )
        customer = Customer.objects.get(id=pk)
        formset = OrderFormSet(
            queryset=Order.objects.none(),
            instance=customer
        )
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
        else:
            return HttpResponse('Your order is incorrect')
