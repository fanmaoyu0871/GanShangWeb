# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-05-03 02:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0021_auto_20170428_0403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favirate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.User')),
            ],
        ),
    ]
