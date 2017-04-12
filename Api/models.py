# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    reg_date = models.DateTimeField('注册时间', auto_now_add=True)
    update_date = models.DateTimeField('更新时间', auto_now=True)

class Banner(models.Model):
    banner_image = models.FileField(upload_to='./')


class Product_Category(models.Model):
    category_name = models.CharField(max_length=30)
    parent_id = models.IntegerField(default=0)

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Product_Category)
    price = models.IntegerField()
    real_price = models.IntegerField()
    product_type = models.CommaSeparatedIntegerField(max_length=100)
    product_detail = models.TextField()

class Product_thumb(models.Model):
    thumb = models.FileField(upload_to='./')