from django.contrib import admin
from .models import Banner
from .models import User
from .models import Product_Category
from .models import Product

# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display = 'banner_image',

class UserAdmin(admin.ModelAdmin):
    list_display = ('phone', 'username')

    def get_readonly_fields(self, request, obj=None):
        return self.fields or [f.name for f in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

class Product_CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent_id', 'category_name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'category_id', 'product_type', 'price', 'real_price')


admin.site.register(Banner, BannerAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Product_Category, Product_CategoryAdmin)
admin.site.register(Product, ProductAdmin)