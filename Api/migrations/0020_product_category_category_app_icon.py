# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-27 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0019_auto_20170427_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_category',
            name='category_app_icon',
            field=models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='app\u5206\u7c7b\u56fe\u7247'),
        ),
    ]
