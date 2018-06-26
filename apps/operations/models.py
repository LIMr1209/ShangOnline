from django.db import models
from datetime import datetime
from users.models import UserProfile
from courses.models import CourseInfo



# Create your models here.

class UserAskInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='咨询姓名')
    phone = models.CharField(max_length=11, verbose_name='咨询手机')
    course = models.CharField(max_length=20, verbose_name='咨询课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '咨询信息'
        verbose_name_plural = verbose_name


class UserLoveInfo(models.Model):
    userinfo = models.ForeignKey(UserProfile, verbose_name='所属用户')
    love_id = models.IntegerField(verbose_name='收藏id')
    love_type = models.IntegerField(choices=((1, '收藏机构'), (2, '收藏课程'), (3, '收藏讲师')), verbose_name='收藏类别')
    love_status = models.BooleanField(default=False, verbose_name='收藏状态')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.userinfo.username

    class Meta:
        verbose_name = '用户收藏信息'
        verbose_name_plural = verbose_name


class UserCourseInfo(models.Model):
    userinfo = models.ForeignKey(UserProfile, verbose_name='所属用户')
    courseinfo = models.ForeignKey(CourseInfo, verbose_name='所属课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.userinfo.username

    class Meta:
        # 字段联合唯一
        unique_together = ('userinfo', 'courseinfo')
        verbose_name = '用户所学课程信息'
        verbose_name_plural = verbose_name


class UserMessageInfo(models.Model):
    userinfo = models.IntegerField(default=0, verbose_name='所属用户')
    message = models.CharField(max_length=200, verbose_name='消息内容')
    msg_status = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = '用户消息信息'
        verbose_name_plural = verbose_name


class UserCommentInfo(models.Model):
    userinfo = models.ForeignKey(UserProfile, verbose_name='所属用户')
    courseinfo = models.ForeignKey(CourseInfo, verbose_name='所属课程')
    comment_content = models.CharField(max_length=200, verbose_name='评论内容')
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    def __str__(self):
        return self.comment_content

    class Meta:
        verbose_name = '用户评论信息'
        verbose_name_plural = verbose_name
