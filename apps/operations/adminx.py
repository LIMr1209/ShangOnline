from .models import UserAskInfo, UserCommentInfo, UserLoveInfo, UserCourseInfo, UserMessageInfo
import xadmin


class UserAskInfoXAdmin(object):
    list_display = ['name', 'phone', 'course', 'add_time']
    search_fields = ['name', 'phone', 'course']
    list_filter = ['name', 'phone', 'course', 'add_time']


class UserCommentInfoXAdmin(object):
    list_display = ['userinfo', 'courseinfo', 'comment_content', 'add_time']
    search_fields = ['userinfo', 'courseinfo', 'comment_content']
    list_filter = ['userinfo', 'courseinfo', 'comment_content', 'add_time']


class UserLoveInfoXAdmin(object):
    list_display = ['userinfo', 'love_id', 'love_type', 'love_status', 'add_time']
    search_fields = ['userinfo', 'love_id', 'love_type', 'love_status']
    list_filter = ['userinfo', 'love_id', 'love_type', 'love_status', 'add_time']


class UserCourseInfoXAdmin(object):
    list_display = ['userinfo', 'courseinfo', 'add_time']
    search_fields = ['userinfo', 'courseinfo']
    list_filter = ['userinfo', 'courseinfo', 'add_time']


class UserMessageInfoXAdmin(object):
    list_display = ['userinfo', 'message', 'msg_status', 'add_time']
    search_fields = ['userinfo', 'message', 'msg_status']
    list_filter = ['userinfo', 'message', 'msg_status', 'add_time']


xadmin.site.register(UserAskInfo, UserAskInfoXAdmin)
xadmin.site.register(UserCommentInfo, UserCommentInfoXAdmin)
xadmin.site.register(UserLoveInfo, UserLoveInfoXAdmin)
xadmin.site.register(UserCourseInfo, UserCourseInfoXAdmin)
xadmin.site.register(UserMessageInfo, UserMessageInfoXAdmin)
