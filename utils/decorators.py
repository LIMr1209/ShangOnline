from django.shortcuts import reverse, redirect
from django.http import JsonResponse


def login_decorator(func):
    def login_handle(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            if request.is_ajax():
                return JsonResponse({
                    'status': 'nologin'
                })
            url = request.get_full_path()
            ret = redirect(reverse('users:user_login'))
            ret.set_cookie('url', url)
            return ret

    return login_handle
