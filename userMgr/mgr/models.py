from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.SmallIntegerField()
    phone = models.CharField(max_length=16,null=True,blank=True)
    addtime = models.DateTimeField(auto_now_add=True)
