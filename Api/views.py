# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from dss.Serializer import serializer  #序列化模块

from .models import User
from .models import Product_Category
from .models import Product

PAGE_SIZE = 20

#{'code':200, 'data':{}, 'msg':'success'}


#-----***************************------------ User  Module ------------***************************---------------------

def code_msg(dict, code, msg):
    dict['code'] = code
    dict['msg'] = msg


def reg(request):
    if (request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        phone = request.POST['phone']
        response = {}
        obj, flag = User.objects.get_or_create(username=username, password=password, phone=phone)
        response['data'] = serializer(obj, datetime_format='string')

        if (not flag):
            code_msg(response, 100, '用户已注册')
        else:
            code_msg(response, 200, '注册成功')

        return HttpResponse(JsonResponse(response), content_type='application/json')


def login(request):
    if(request.method == 'POST'):
        phone = request.POST['phone']
        password = request.POST['password']
        response = {}

        try:
            obj = User.objects.get(phone=phone)
        except ObjectDoesNotExist:
            code_msg(response, 100, '用户不存在')
        else:
            if(password == obj.password):
                code_msg(response, 200, '登录成功')
                response['data'] = serializer(obj, datetime_format='string')
            else:
                code_msg(response, 100, '密码错误')

        return HttpResponse(JsonResponse(response), content_type='application/json')

def changePassword(request):
    if(request.method == 'POST'):
        phone = request.POST['phone']
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        response = {}

        try:
            obj = User.objects.get(phone=phone)
        except ObjectDoesNotExist:
            code_msg(response, 100, '用户不存在')
        else:
            update_num = User.objects.filter(phone=phone).update(password=new_password)
            if(update_num == 1):
                code_msg(response, 200, '密码更新成功')
            else:
                code_msg(response, 500, '数据库更新密码出错')

        return HttpResponse(JsonResponse(response), content_type='application/json')


#-----***************************------------ Product  Module ------------***************************---------------------
def categorys(request):
    qs = Product_Category.objects.filter(parent_id=0)
    response = {}

    if(qs.exists()):
        response['data'] = serializer(qs)
        code_msg(response, 200, '获取分类成功')
    else:
        code_msg(response, 100, '分类不存在')

    return HttpResponse(JsonResponse(response), content_type='application/json')

def list_product(request, page):
    category_id = request.POST['category_id']
    response = {}

    if(not category_id):
        code_msg(response, 100, '参数错误：未传分类id')
    else:
        qs = Product_Category.objects.filter(parent_id = category_id)
        li = [obj.pk for obj in qs]
        qs = Product.objects.filter(category_id__in = li)[(int(page)-1)*PAGE_SIZE:int(page)*PAGE_SIZE]
        response['data'] = serializer(qs)
        code_msg(response, 200, '获取产品列表成功')

    return HttpResponse(JsonResponse(response), content_type='application/json')

