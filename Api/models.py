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
class Advantise(models.Model):
    title = models.CharField('广告名称', max_length=30, default='')
    ad_image = models.ImageField(upload_to='./')

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Banner(models.Model):
    title = models.CharField('名称', max_length=30, default='')
    banner_image = models.ImageField(upload_to='./')

    def __str__(self):
        return self.title

@python_2_unicode_compatible
class Product_Category(models.Model):
    category_name = models.CharField('分类名称', max_length=30)
    parent_id = models.IntegerField('父分类id', default=0)
    category_ad_img = models.ImageField('分类广告图片', null=True, blank=True)
    category_app_big_icon = models.ImageField('app分类大图标', null=True, blank=True)
    category_app_small_icon = models.ImageField('app分类小图标', null=True, blank=True)

    def __str__(self):
        return self.category_name

@python_2_unicode_compatible
class Product(models.Model):
    product_name = models.CharField('产品名称', max_length=100)
    product_thumb = models.ImageField(upload_to='./', null=True, blank=True)
    product_intro = models.CharField('产品简介', max_length=20, null=True, blank=True)
    product_sum_sal = models.IntegerField('总销量', default=0)
    product_favorite_count = models.IntegerField('收藏数量', default=0)
    rest_count = models.IntegerField('库存数量', default=0)
    zhibao_year = models.IntegerField('质保时间', default=1)
    category = models.ForeignKey(Product_Category)
    price = models.IntegerField('价格')
    real_price = models.IntegerField('促销价格', null=True, blank=True, default=0)
    product_type = models.CharField('产品类型', max_length=50, null=True, blank=True)
    product_detail = UEditorField('产品细节', height=300, width=1000,
                                  default=u'', blank=True, imagePath="./images/",
                                  toolbars='besttome', filePath='./files/')

    def __str__(self):
        return self.product_name

@python_2_unicode_compatible
class Product_image(models.Model):
    thumb = models.ImageField(upload_to='./')
    product_id = models.ForeignKey(Product)

    def __str__(self):
        return str(self.product_id)

@python_2_unicode_compatible
class ShopCar(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    count = models.IntegerField('数量', default=1)
    price = models.IntegerField('价格', default=0)

    def __str__(self):
        return str(self.product)

@python_2_unicode_compatible
class Favirate(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)

    def __str__(self):
        return self.id

# @python_2_unicode_compatible
# class Order(models.Model):
