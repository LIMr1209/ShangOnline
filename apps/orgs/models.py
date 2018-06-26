from django.db import models
from datetime import datetime
from DjangoUeditor.models import UEditorField


# Create your models here.

class CityInfo(models.Model):
    name = models.CharField(max_length=50, verbose_name='城市名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '城市信息'
        verbose_name_plural = verbose_name


class OrgInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='机构名称')
    image = models.ImageField(upload_to='org/%y/%m', verbose_name='机构图片', max_length=100)
    study_num = models.IntegerField(default=0, verbose_name='学习人数')
    address = models.CharField(max_length=200, verbose_name='机构地址')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    love_num = models.IntegerField(default=0, verbose_name='收藏数')
    desc = models.CharField(max_length=200, verbose_name='机构简介')
    detail = UEditorField(verbose_name='机构详情', width=700, height=400, toolbars='full',
                          imagePath='ueditor/images/', filePath='ueditor/files/',
                          upload_settings={'imageMaxSizing': 1024000},
                          default='')
    course_num = models.IntegerField(default=0, verbose_name='课程数量')
    cityinfo = models.ForeignKey(CityInfo, verbose_name='所属城市')
    category = models.CharField(choices=(('jg', '机构'), ('gx', '高校'), ('gr', '个人')), max_length=5, verbose_name='机构类别',
                                null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '机构信息'
        verbose_name_plural = verbose_name


class TeacherInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name='讲师姓名')
    image = models.ImageField(upload_to='teacher/%y%m', verbose_name='讲师头像', null=True, blank=True, max_length=200)
    work_year = models.IntegerField(default=3, verbose_name='工作年限')
    work_company = models.CharField(max_length=20, verbose_name='就职公司', null=True, blank=True)
    work_position = models.CharField(max_length=20, verbose_name='工作职位', null=True, blank=True)
    age = models.IntegerField(default=30, verbose_name='讲师年龄')
    work_style = models.CharField(max_length=20, verbose_name='教学特点', null=True, blank=True)
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    love_num = models.IntegerField(default=0, verbose_name='收藏数')
    orginfo = models.ForeignKey(OrgInfo, verbose_name='所属机构')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '讲师信息'
        verbose_name_plural = verbose_name
