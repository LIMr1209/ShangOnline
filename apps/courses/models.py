from django.db import models
from datetime import datetime
from orgs.models import OrgInfo, TeacherInfo
from DjangoUeditor.models import UEditorField

# Create your models here.

class CourseInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='课程名称')
    desc = models.CharField(max_length=200, verbose_name='课程简介')
    detail = UEditorField(verbose_name='课程详情', width=700, height=400, toolbars='full',
                          imagePath='ueditor/images/', filePath='ueditor/files/',
                          upload_settings={'imageMaxSizing': 1024000},
                          default='')
    level = models.CharField(choices=(('初级', '初级'), ('中级', '中级'), ('高级', '高级')), max_length=5, verbose_name='课程难度',
                             default='初级')
    stu_num = models.IntegerField(default=0, verbose_name='学习人数')
    study_time = models.IntegerField(default=0, verbose_name='学习时长')
    lesson_num = models.IntegerField(default=0, verbose_name='章节数')
    category = models.CharField(choices=(('前端', '前端'), ('后台', '后台')), max_length=5, verbose_name='课程类别')
    image = models.ImageField(upload_to='course/%y/%m', verbose_name='课程图片', max_length=100)
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    love_num = models.IntegerField(default=0, verbose_name='收藏数')
    orginfo = models.ForeignKey(OrgInfo, verbose_name='所属机构')
    teacherinfo = models.ForeignKey(TeacherInfo, verbose_name='所属讲师')
    need_know = models.CharField(max_length=100, verbose_name='课程须知', null=True, blank=True)
    teacher_say = models.CharField(max_length=200, verbose_name='老师告知', null=True, blank=True)
    is_banner = models.BooleanField(default=False,verbose_name='是否轮播')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '课程信息'
        verbose_name_plural = verbose_name


class LessonInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='章节名称')
    courseinfo = models.ForeignKey(CourseInfo, verbose_name='所属课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '章节信息'
        verbose_name_plural = verbose_name


class VideoInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='视频名称')
    study_time = models.IntegerField(default=0, verbose_name='视频时长')
    url = models.URLField(
        default='http://video.atguigu.com/ce182d3e92d24c08ada798ed75236efe/64240d5f98c849d7a48a701646314ef0-abb0a550e0a4e1bd89390a178f91a577-ld.mp4',
        max_length=200, verbose_name='视频链接')
    lessoninfo = models.ForeignKey(LessonInfo, verbose_name='所属章节')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '视频信息'
        verbose_name_plural = verbose_name


class SourceInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='资源名称')
    file_add = models.FileField(upload_to='source/%y/%m', max_length=100, verbose_name='资源地址')
    courseinfo = models.ForeignKey(CourseInfo, verbose_name='所属课程')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '资源信息'
        verbose_name_plural = verbose_name
