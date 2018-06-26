from .models import EmailVerify, Banner
import xadmin
from xadmin import views


class BaseXAdminSettings(object):
    enable_themes = True
    use_bootswath = True


class GlobalSiteSettings(object):
    site_title = '尚在线后台管理系统'
    site_footer = '尚硅谷IT教育'
    menu_style = 'accordion'  # 菜单折叠


class EmailVerifyXAdmin(object):
    list_display = ['email', 'code', 'send_type', 'add_time']
    search_fields = ['email', 'code', 'send_type']
    list_filter = ['email', 'code', 'send_type', 'add_time']
    model_icon = 'fa fa-bandcamp'  # 菜单图标


class BannerXAdmin(object):
    list_display = ['image', 'url', 'add_time']
    search_fields = ['image', 'url']
    list_filter = ['image', 'url']


xadmin.site.register(EmailVerify, EmailVerifyXAdmin)
xadmin.site.register(Banner, BannerXAdmin)
xadmin.site.register(views.BaseAdminView, BaseXAdminSettings)
xadmin.site.register(views.CommAdminView, GlobalSiteSettings)
