# 规范：系统包在最上头，第三方包在中间，自己的包在最下

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

'''
AbstractUser:
- username 用户名, password 密码, email 邮箱, first_name 名字, last_name 姓氏, is_staff 是否管理员
- create() 创建普通用户, create_user() 创建密码带加密的用户, create_superuser() 创建管理员, set_password(pwd) 设置密码
注: 需在 settings.py 中添加 AUTH_USER_MODEL = 'users.UserProfile' 语句, 覆盖django默认的表, 自己的表才会生效
'''


class UserProfile(AbstractUser):
    '''用户档案 UserProfile'''

    name = models.CharField(max_length=30, default="", verbose_name="名称")
    birthday = models.DateField(null=True, blank=True, verbose_name="出生日期")
    # 注：null：数据库中该字段允许为空；blank：表单验证是允许为空。
    mobile = models.CharField(max_length=11, verbose_name="手机号码")
    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), default="male", verbose_name="性别")
    desc = models.CharField(max_length=80, null=True, blank=True, verbose_name="描述")

    class Meta:
        # db_table = "users_userprofile"  # 指定表名（默认app名+类名）
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    # 注：verbose_name指在django自带admin管理界面中显示的字段名。verbose_name是单数形式，verbose_name_plural是复数形式。

    def __str__(self):
        return self.name  # 可简单理解为设置 print() 的输出值


class VerifyCode(models.Model):
    '''短信验证码'''

    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="手机号码")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="时间")
    # 注：datetime.now()是编译时间，datetime.now是当前时间

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
