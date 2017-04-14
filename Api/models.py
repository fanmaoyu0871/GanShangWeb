# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from DjangoUeditor.models import UEditorField
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class User(models.Model):
    username = models.CharField('昵称', max_length=20, null=True, blank=True)
    phone = models.CharField('手机号', max_length=11, null=True, blank=True)
    password = models.CharField('密码', max_length=200, null=True, blank=True)
    reg_date = models.DateTimeField('注册时间', auto_now_add=True)
    update_date = models.DateTimeField('更新时间', auto_now=True)

    def __str__(self):
        return self.username if len(self.username)>0 else self.phone

@python_2_unicode_compatible
class Banner(models.Model):
    banner_image = models.FileField(upload_to='./')

    def __str__(self):
        return self.banner_image

@python_2_unicode_compatible
class Product_Category(models.Model):
    category_name = models.CharField('分类名称', max_length=30)
    parent_id = models.IntegerField('父分类id', default=0)

    def __str__(self):
        return self.category_name

@python_2_unicode_compatible
class Product(models.Model):
    product_name = models.CharField('产品名称', max_length=100)
    category = models.ForeignKey(Product_Category)
    price = models.IntegerField('价格')
    real_price = models.IntegerField('促销价格', null=True, blank=True)
    product_type = models.CommaSeparatedIntegerField('产品类型', max_length=100, null=True, blank=True)
    product_detail = UEditorField('产品细节', height=300, width=1000,
                                  default=u'', blank=True, imagePath="upload/images/",
                                  toolbars='besttome', filePath='upload/files/')

    def __str__(self):
        return self.product_name

@python_2_unicode_compatible
class Product_thumb(models.Model):
    thumb = models.FileField(upload_to='./')

    def __str__(self):
        return self.thumb