from django.contrib import admin

from .models import Customer
from .models import Order
from .models import Product
from .models import Tag


# 注册模型，使admin可直接操作
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Tag)
