from django.contrib import admin

# Register your models here.
from myapp.models import User
# 1.普通写法
# admin.site.register(Users)
# 2.装饰器写法
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # 设置要显示的字段
    list_display = ('id','name','age','time')
    # 设置默认可编辑字段
    # list_editable = ['name']
    # 设置哪些字段可编辑
    list_display_links = ('name','age')
    # 设置每页显示多少条记录 （默认100条）
    list_per_page = 5
    # 设置默认排序字段
    ordering = ('id',) # -id 表示降序


