# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-21 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_merge_20180621_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseinfo',
            name='need_know',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='课程须知'),
        ),
    ]
