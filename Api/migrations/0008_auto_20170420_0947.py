# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-20 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0007_advantise'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_sum_sal',
            field=models.IntegerField(default=0, verbose_name='\u603b\u9500\u91cf'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_thumb',
            field=models.FileField(blank=True, null=True, upload_to='./'),
        ),
    ]
