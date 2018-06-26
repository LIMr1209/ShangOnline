# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-21 11:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_is_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='学生地址'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user/%y/%m', verbose_name='学生头像'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='学生手机'),
        ),
    ]
