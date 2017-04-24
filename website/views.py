# -*- coding:utf-8 -*-

from django.shortcuts import render
from Api.models import Banner
from Api.models import Product_Category
from Api.models import Advantise
from Api.models import Product

from dss.Serializer import serializer  #序列化模块
import json

# Create your views here.

def index(request):

    #banner list
    banner_list = Banner.objects.all()

    #category list
    parent_list = Product_Category.objects.filter(parent_id=0)
    cate_list =[]

    for cate in parent_list:
        response = {}
        response['parent'] = cate
        qs = Product_Category.objects.filter(parent_id = cate.pk)
        response['child'] = qs

        cate_list.append(response)

    #ad list
    ad_list = Advantise.objects.all()

    #good product , order by column of 'product_sum_sale'
    good_list = Product.objects.all().order_by('-product_sum_sal')

    #product list
    product_list = []
    for cate in parent_list:
        response = {}
        response['parent'] = cate
        qs = Product_Category.objects.filter(parent_id=cate.pk)
        li = [obj.pk for obj in qs]
        qs = Product.objects.filter(category_id__in=li)
        response['child'] = list(qs)
        response['id'] = cate.pk
        product_list.append(response)


    return render(request, 'index.html', {'banner_list':list(banner_list),
                                          'cate_list':cate_list,
                                          'ad_list':list(ad_list),
                                          'good_list':list(good_list),
                                          'product_list':list(product_list),
                                           'product_list_json': json.dumps(serializer(product_list))})

def category_view(request):
    category_id = request.GET['category_id']
    product_list = Product.objects.filter(category_id = category_id)

    return render(request, 'search_list.html', {'product_list':list(product_list)})

def search_list(request):
    condition = request.GET['search']
    product_list = Product.objects.filter(product_name__contains=condition)

    return render(request, 'search_list.html', {'product_list':list(product_list),
                                                'condition':condition,
                                                'count':len(product_list)})
