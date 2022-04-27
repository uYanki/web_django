from django.urls import path,re_path,re_path
from . import views # 导入同目录下的views
urlpatterns = [
    path('',views.index,name="index"),
    path('articles/<int:year>/<int:month>/', views.articles,name="articles"),
    re_path(r'^blogs/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.blogs),
    path('page/',views.pages,),
    path('reverse/',views.func),
    # path('page/<int:value>/',views.pages),
]