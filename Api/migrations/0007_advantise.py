# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-20 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0006_banner_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30, verbose_name='\u5e7f\u544a\u540d\u79f0')),
                ('ad_image', models.FileField(upload_to='./')),
            ],
        ),
    ]
