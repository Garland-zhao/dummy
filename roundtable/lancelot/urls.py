from django.urls import path

from lancelot.views.home import HomePage, UserPage
from lancelot.views.order import (
    AccountSettings,
    ProductsPage,
    CustomerPage,
    OrderPage,
)
from lancelot.views.user import RegisterPage, LoginPage, logoutUser


urlpatterns = [
    # 注册、登录、登出
    path('register/', RegisterPage.as_view(), name='register'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', logoutUser, name="logout"),
    # 管理员/用户基础页面
    path('', HomePage.as_view(), name="home"),
    path('user/', UserPage.as_view(), name="user_page"),
    # 用户修改用户名（昵称）
    path('account/', AccountSettings.as_view(), name="account"),
    # 商品和订单
    path('products/', ProductsPage.as_view(), name='products'),
    path('customer/<str:pk>/', CustomerPage.as_view(), name="customer"),
    path('create_order/<str:pk>', OrderPage.as_view(), name='create_order'),
]
