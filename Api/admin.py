# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Banner
from .models import User
from .models import Product_Category
from .models import Product
from .models import Advantise
from .models import Product_image
from .models import Favirate


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
    list_display = ('id', 'product_name', 'category_id', 'product_type', 'price', 'real_price')

class AdvantiseAdmin(admin.ModelAdmin):
    list_display = ('title', 'ad_image')

class Product_imageAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'thumb')

class FavirateAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')
    


admin.site.register(Banner, BannerAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Product_Category, Product_CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Product_image, Product_imageAdmin)
admin.site.register(Advantise, AdvantiseAdmin)
admin.site.register(Favirate, FavirateAdmin)