# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-21 11:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='category',
            field=models.CharField(choices=[('前端', '前端'), ('后台', '后台')], max_length=5, verbose_name='课程类别'),
        ),
        migrations.AlterField(
            model_name='courseinfo',
            name='level',
            field=models.CharField(choices=[('初级', '初级'), ('中级', '中级'), ('高级', '高级')], default='初级', max_length=5, verbose_name='课程难度'),
        ),
        migrations.AlterField(
            model_name='videoinfo',
            name='lessoninfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.LessonInfo', verbose_name='所属章节'),
        ),
    ]
