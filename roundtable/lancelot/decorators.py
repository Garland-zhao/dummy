"""装饰器文件"""
from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_roles=['customer']):
	"""视图函数访问权限指定校验"""
	def decorator(view_func):
		def wrapper_func(request, *args, **kwargs):
			# 从请求中获取用户身份
			group = None
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name

			# 对于符合该视图的用户，可以继续访问，否则返回权限错误提示
			if group in allowed_roles:
				return view_func(request, *args, **kwargs)
			else:
				return HttpResponse('You are not authorized to view this page')
		return wrapper_func

	return decorator


def admin_only(view_func):
	"""管理员访问权限"""
	def wrapper_function(request, *args, **kwargs):
		# 从请求中获取用户身份
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		# 一般用户跳转到'用户页'
		if group == 'customer':
			return redirect('user_page')

		# 管理员可以全局访问
		elif group == 'admin':
			return view_func(request, *args, **kwargs)
		
		# 还可补充其它身份的跳转
		else:
			return HttpResponse('You are not authorized to view this page')

	return wrapper_function