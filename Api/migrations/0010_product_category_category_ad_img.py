# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-20 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0009_product_product_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_category',
            name='category_ad_img',
            field=models.FileField(blank=True, null=True, upload_to=b'', verbose_name='\u5206\u7c7b\u5e7f\u544a\u56fe\u7247'),
        ),
    ]