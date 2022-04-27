"""uykshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# 静态资源配置
from django.conf.urls import url
from uykshop.settings import MEDIA_ROOT
from django.views.static import serve

from django.conf.urls import include
from rest_framework.documentation import include_docs_urls

from goods.views import GoodsListView
# from goods.views_base import GoodsListView

from goods.views import GoodsListViewSet
# good_list = GoodsListViewSet.as_view({
#     'get': 'list',
#     # 'post': 'create'
# }) # 用router代替
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'goods_ex', GoodsListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),  # 静态资源配置

    url(r'goods/$', GoodsListView.as_view(), name="goods-list"),
    # url(r'goods_ex/$', good_list, name="goods-list-ex"),
    url(r'^', include(router.urls)),

    # url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework")),  # 开启登录功能
    url(r'docs/$', include_docs_urls(title="mydocs"))

]
