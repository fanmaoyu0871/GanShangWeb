"""GanShangWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Api import views as api
from DjangoUeditor import urls as DjangoUeditor_urls
from website import views as Site_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include(DjangoUeditor_urls)),

    #api
    url(r'^api/v1/user/reg/$', api.reg),
    url(r'^api/v1/user/login/$', api.login),
    url(r'^api/v1/user/changePassword/$', api.changePassword),
    url(r'^api/v1/user/favirate_list/$', api.favirate_list),
    url(r'^api/v1/product/categorys/$', api.categorys),
    url(r'^api/v1/product/list_product/$', api.list_product),
    url(r'^api/v1/product/shouye_list/$', api.shouye_list),
    url(r'^api/v1/shopcar/[A-Za-z]+/$', api.shopcar_update),
    url(r'^api/v1/product/favirate/$', api.favirate_op),

    #web site
    url(r'^$', Site_views.index, name='index'),
    url(r'^category/$', Site_views.category_view, name='category_view'),
    url(r'^search/$', Site_views.search_list, name='search_list'),
    url(r'^product/filter/$', Site_views.product_filter_price, name='product_filter_price'),
    url(r'^product/$', Site_views.product_detail, name='product_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

