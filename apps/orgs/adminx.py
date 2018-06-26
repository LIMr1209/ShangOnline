import xadmin
from .models import CityInfo, TeacherInfo, OrgInfo


class CityInfoXAdmin(object):
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['name', 'add_time']


class OrgInfoXAdmin(object):
    list_display = ['name', 'image', 'study_num', 'address', 'click_num', 'love_num', 'desc', 'detail', 'cityinfo',
                    'add_time']
    search_fields = ['name', 'image', 'study_num', 'address', 'click_num', 'love_num', 'cityinfo']
    list_filter = ['name', 'image', 'study_num', 'address', 'click_num', 'love_num', 'desc', 'detail', 'cityinfo',
                   'add_time']
    style_fields = {'detail': 'ueditor'}


class TeacherInfoXAdmin(object):
    list_display = ['name', 'image', 'work_year', 'work_company', 'work_position', 'age', 'work_style', 'click_num',
                    'love_num',
                    'orginfo', 'add_time']
    search_fields = ['name', 'image', 'work_year', 'work_company', 'work_position', 'age', 'work_style', 'click_num',
                     'love_num',
                     'orginfo']
    list_filter = ['name', 'image', 'work_year', 'work_company', 'work_position', 'age', 'work_style', 'click_num',
                   'love_num',
                   'orginfo', 'add_time']


xadmin.site.register(CityInfo, CityInfoXAdmin)
xadmin.site.register(OrgInfo, OrgInfoXAdmin)
xadmin.site.register(TeacherInfo, TeacherInfoXAdmin)
