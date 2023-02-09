from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View

from lancelot.decorators import allowed_users, admin_only
from lancelot.models import Customer, Order


class HomePage(View):
    """管理员主页（查看所有用户和订单）"""

    @method_decorator(admin_only)
    def get(self, request):
        orders = Order.objects.all()
        customers = Customer.objects.all()
        total_orders = orders.count()
        delivered = orders.filter(status='Delivered').count()
        pending = orders.filter(status='Pending').count()

        context = {
            'orders': orders,
            'customers': customers,
            'total_orders': total_orders,
            'delivered': delivered,
            'pending': pending,
        }

        return render(request, 'lancelot/dashboard.html', context)


class UserPage(View):
    """客户主页（查看自己的订单）"""

    # 指定仅'客户'身份访问，方便日后增加其它身份或逻辑
    @method_decorator(allowed_users(allowed_roles=['customer']))
    def get(self, request):
        orders = request.user.customer.order_set.all()
        total_orders = orders.count()
        delivered = orders.filter(status='Delivered').count()
        pending = orders.filter(status='Pending').count()

        context = {
            'orders': orders,
            'total_orders': total_orders,
            'delivered': delivered,
            'pending': pending
        }

        return render(request, 'lancelot/user.html', context)
