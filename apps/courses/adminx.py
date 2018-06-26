import xadmin
from .models import CourseInfo, LessonInfo, VideoInfo, SourceInfo


class CourseInfoXAdmin(object):
    list_display = ['name', 'desc', 'detail', 'level', 'stu_num', 'study_time', 'lesson_num', 'category', 'image',
                    'click_num', 'love_num', 'orginfo', 'teacherinfo', 'add_time']
    search_fields = ['name', 'desc', 'detail', 'level', 'stu_num', 'study_time', 'lesson_num', 'category', 'image',
                     'click_num', 'love_num', 'orginfo', 'teacherinfo']
    list_filter = ['name', 'desc', 'detail', 'level', 'stu_num', 'study_time', 'lesson_num', 'category', 'image',
                   'click_num', 'love_num', 'orginfo', 'teacherinfo', 'add_time']
    style_fields = {'detail': 'ueditor'}

class LessonInfoXAdmin(object):
    list_display = ['name', 'courseinfo', 'add_time']
    search_fields = ['name', 'courseinfo']
    list_filter = ['name', 'courseinfo', 'add_time']


class VideoInfoXAdmin(object):
    list_display = ['name', 'study_time', 'url', 'lessoninfo', 'add_time']
    search_fields = ['name', 'study_time', 'url', 'lessoninfo']
    list_filter = ['name', 'study_time', 'url', 'lessoninfo', 'add_time']


class SourceInfoXAdmin(object):
    list_display = ['name', 'file_add', 'courseinfo', 'add_time']
    search_fields = ['name', 'file_add', 'courseinfo']
    list_filter = ['name', 'file_add', 'courseinfo', 'add_time']


xadmin.site.register(CourseInfo, CourseInfoXAdmin)
xadmin.site.register(LessonInfo, LessonInfoXAdmin)
xadmin.site.register(VideoInfo, VideoInfoXAdmin)
xadmin.site.register(SourceInfo, SourceInfoXAdmin)
