# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-21 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0010_product_category_category_ad_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_thumb',
            field=models.ImageField(blank=True, null=True, upload_to='./'),
        ),
    ]
