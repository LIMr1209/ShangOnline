# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-25 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_courseinfo_teacher_say'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinfo',
            name='is_banner',
            field=models.BooleanField(default=False, verbose_name='是否轮播'),
        ),
    ]
