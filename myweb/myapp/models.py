from django.db import models

# Create your models here.

from django.db import models
from datetime import datetime
class User(models.Model):
    name = models.CharField('名字',max_length=32)
    age = models.IntegerField('年龄',default=20)
    time = models.DateTimeField('日期',default=datetime.now)
    def __str__(self):
        return "%s %d"%(self.name,self.age)
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息管理'