# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-21 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0011_auto_20170421_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advantise',
            name='ad_image',
            field=models.ImageField(upload_to='./'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='banner_image',
            field=models.ImageField(upload_to='./'),
        ),
        migrations.AlterField(
            model_name='product_category',
            name='category_ad_img',
            field=models.ImageField(blank=True, null=True, upload_to=b'', verbose_name='\u5206\u7c7b\u5e7f\u544a\u56fe\u7247'),
        ),
    ]