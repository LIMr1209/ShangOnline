from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=20, verbose_name='用户昵称', default='')
    birthday = models.DateField(null=True, blank=True, verbose_name='用户生日')
    gender = models.CharField(choices=(('girl', '女'), ('boy', '男')), verbose_name='用户性别', max_length=5, default='girl')
    address = models.CharField(max_length=200, verbose_name='学生地址', null=True, blank=True)
    phone = models.CharField(max_length=11, verbose_name='学生手机', null=True, blank=True)
    is_start = models.BooleanField(default=False, verbose_name='是否激活')
    image = models.ImageField(upload_to='user/%y/%m', verbose_name='学生头像', max_length=100, null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return self.username

    # 用户未读消息数
    def get_msg_count(self):
        from operations.models import UserMessageInfo
        return UserMessageInfo.objects.filter(userinfo=self.id, msg_status=False).count()

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name


class EmailVerify(models.Model):
    email = models.EmailField(max_length=100, verbose_name='邮箱')
    code = models.CharField(max_length=20, verbose_name='验证码')
    send_type = models.CharField(choices=(('register', '注册'), ('forget', '修改'), ('change_email', '修改邮箱')),
                                 max_length=20,
                                 verbose_name='验证码类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name


class Banner(models.Model):
    image = models.ImageField(upload_to='banner/%y/%m', max_length=100, verbose_name='轮播图')
    url = models.URLField(max_length=100, verbose_name='轮播图片链接', default='http://www.atguigu.com/')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name = '轮播图信息'
        verbose_name_plural = verbose_name
