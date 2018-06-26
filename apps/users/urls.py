"""ShangOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import user_register, user_login, user_logout, user_active, user_forget, user_reset, user_info, \
    user_change_image, user_change_info, user_change_password, user_mycourse, user_loveorg, user_message, \
    user_send_code, user_loveteacher,user_lovecourse,user_change_email,user_readmsg

urlpatterns = [
    url(r'^user_register/$', user_register, name='user_register'),
    url(r'^user_login/$', user_login, name='user_login'),
    url(r'^user_logout/$', user_logout, name='user_logout'),
    url(r'^active/(\w+)/$', user_active, name='user_active'),
    url(r'^user_forget/$', user_forget, name='user_forget'),
    url(r'^user_reset/(\w+)/$', user_reset, name='user_reset'),

    url(r'^user_info/$', user_info, name='user_info'),
    url(r'^user_change_image/$', user_change_image, name='user_change_image'),
    url(r'^user_change_info/$', user_change_info, name='user_change_info'),
    url(r'^user_change_password/$', user_change_password, name='user_change_password'),
    url(r'^user_send_code/$', user_send_code, name='user_send_code'),
    url(r'^user_change_email/$', user_change_email, name='user_change_email'),
    url(r'^user_mycourse/$', user_mycourse, name='user_mycourse'),
    url(r'^user_loveorg/$', user_loveorg, name='user_loveorg'),
    url(r'^user_loveteacher/$', user_loveteacher, name='user_loveteacher'),
    url(r'^user_lovecourse/$', user_lovecourse, name='user_lovecourse'),
    url(r'^user_message/$', user_message, name='user_message'),
    url(r'^user_readmsg/$',user_readmsg,name='user_readmsg')

]
