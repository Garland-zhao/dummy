from django.conf import settings
from django.shortcuts import redirect


class LoginRequiredMiddleware:
    """登录状态校验中间件"""

    # 登录url
    LOGIN_URL = '/lancelot/login/'

    # 无需校验登录状态的url
    OPEN_URLS = [
        '/lancelot/login/',
        '/lancelot/logout/',
        '/lancelot/register/',
        'swagger/',
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """根据用户登录状态判断是否需要跳转到登录页面"""
        if not request.user.is_authenticated and request.path_info not in self.OPEN_URLS:
            return redirect(self.LOGIN_URL + '?next=' + request.path)

        return self.get_response(request)