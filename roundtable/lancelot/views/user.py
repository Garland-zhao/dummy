"""用户注册、登录、登出"""
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from lancelot.forms import CreateUserForm


class RegisterPage(View):
    """用户注册"""

    def get(self, request):
        """渲染注册页"""
        form = CreateUserForm()
        context = {'form': form}
        return render(request, 'lancelot/register.html', context)

    def post(self, request):
        """处理用户注册信息, 校验正确后入库"""
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect('login')
        else:
            context = {'form': form}
            return render(request, 'lancelot/register.html', context)


class LoginPage(View):
    """用户登录"""

    def get(self, request):
        """渲染登录页"""
        context = {}
        return render(request, 'lancelot/login.html', context)
  
    def post(self, request):
        """校验用户输入的用户名和密码"""
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            context = {}
            return render(request, 'lancelot/login.html', context)


def logoutUser(request):
    """用户登出"""
    logout(request)
    return redirect('login')
