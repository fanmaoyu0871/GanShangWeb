# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-13 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_auto_20170412_1025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AlterField(
            model_name='product_category',
            name='category_name',
            field=models.CharField(max_length=30, verbose_name='\u5206\u7c7b\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='product_category',
            name='parent_id',
            field=models.IntegerField(default=0, verbose_name='\u7236\u5206\u7c7bid'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='\u5bc6\u7801'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='\u624b\u673a\u53f7'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='\u6635\u79f0'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
