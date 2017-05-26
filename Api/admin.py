# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Banner
from .models import User
from .models import Product_Category
from .models import Product
from .models import Advantise
from .models import Product_image
from .models import Favirate
from .models import Order
from .models import Status
from .models import ShopCar
from .models import Order_child
from .models import All_attribute
from .models import Product_attribut


import sys

reload(sys)
sys.setdefaultencoding("utf-8")

# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'banner_image')

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'username')

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

class Product_CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent_id', 'category_name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category_id', 'price', 'real_price')

class AdvantiseAdmin(admin.ModelAdmin):
    list_display = ('title', 'ad_image')

class Product_imageAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'thumb')

class FavirateAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_id')

class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')

class ShopCarAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'count')

class Order_childAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'attr_values')

class All_attributeAdmin(admin.ModelAdmin):
    list_display = 'attr_name',

class Product_attributAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'attr_value')
    


admin.site.register(Banner, BannerAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Product_Category, Product_CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Product_image, Product_imageAdmin)
admin.site.register(Advantise, AdvantiseAdmin)
admin.site.register(Favirate, FavirateAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(ShopCar, ShopCarAdmin)
admin.site.register(Order_child, Order_childAdmin)
admin.site.register(All_attribute, All_attributeAdmin)
admin.site.register(Product_attribut, Product_attributAdmin)