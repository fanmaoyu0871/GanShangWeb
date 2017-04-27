# -*- coding:utf-8 -*-

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from Api.models import Banner
from Api.models import Product_Category
from Api.models import Advantise
from Api.models import Product
from Api.models import Product_image

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
    cate = Product_Category.objects.get(pk = category_id)
    if (cate.parent_id != 0):
        search_list = list(Product.objects.filter(category_id=category_id))
    else:
        # product list
        qs = Product_Category.objects.filter(parent_id=cate.pk)
        li = [obj.pk for obj in qs]
        qs = Product.objects.filter(category_id__in=li)
        search_list = list(qs)

    # category list
    parent_list = Product_Category.objects.filter(parent_id=0)

    # product list
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


    return render(request, 'search_list.html', {'search_list':search_list,
                                                'product_list': list(product_list),
                                                'product_list_json': json.dumps(serializer(product_list))})


def search_list(request):
    condition = request.GET['search']
    search_list = Product.objects.filter(product_name__contains=condition)

    # category list
    parent_list = Product_Category.objects.filter(parent_id=0)

    # product list
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

    return render(request, 'search_list.html', {'product_list':list(product_list),
                                                'product_list_json': json.dumps(serializer(product_list)),
                                                'condition':condition,
                                                'count':len(search_list),
                                                'search_list':list(search_list),
                                                'condition_json':json.dumps(condition)})

def product_detail(request):
    product_id = request.GET['product_id']
    product = Product.objects.get(pk = product_id)

    #parse type list
    type_list = product.product_type.split(',')

    #thumb list
    thumb_list = Product_image.objects.filter(product_id = product_id)

    # category list
    parent_list = Product_Category.objects.filter(parent_id=0)

    # product list
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

    return render(request, 'product_detail.html', {'product_list': list(product_list),
                                                   'product_list_json': json.dumps(serializer(product_list)),
                                                   'thumb_list': list(thumb_list),
                                                   'first_thumb': thumb_list[0] if thumb_list else None,
                                                   'product': product,
                                                   'type_list': type_list})

#价格筛选api
def product_filter_price(request):
    min_price = request.GET['fastPrice']
    max_price = request.GET['lastPrice']
    condition = request.GET['search']

    if(condition is None):
        product_list = Product.objects.filter(price__range=(min_price, max_price))
    else:
        product_list = Product.objects.filter(product_name__contains=condition).filter(price__range=(min_price, max_price))

    qs = serializer(product_list)

    return HttpResponse(JsonResponse({'product_list_json': qs}), content_type='application/json')
