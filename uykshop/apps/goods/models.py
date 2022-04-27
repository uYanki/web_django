from asyncio.windows_events import NULL
from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class GoodsCategory(models.Model):
    '''商品类别'''
    category_type = ((1, "一级类目"), (2, "二级类目"), (3, "三级类目"))
    name = models.CharField(max_length=30, verbose_name="类别名", help_text="类别名")
    desc = models.TextField(max_length=200, null=True, blank=True, verbose_name="类别描述", help_text="类别描述")
    code = models.CharField(max_length=30, verbose_name="类别编码", help_text="类别编码")
    type = models.CharField(max_length=30, choices=category_type, verbose_name="类目级别", help_text="类目级别")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="父类别", related_name="sub_cat", on_delete=NULL)  # related_name 用于查询
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "商品类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsBrand(models.Model):
    '''品牌'''
    name = models.CharField(max_length=30, verbose_name="品牌名", help_text="品牌名")
    image = models.ImageField(max_length=200, upload_to="brands/", verbose_name="商标")
    # image 实际上在数据库存储的是char，所以设置max_length

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    '''商品'''
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="商品类目")
    '''
    on_delete=None, # 删除关联表中的数据时,当前表与其关联的field的行为
    on_delete=models.CASCADE, # 删除关联数据,与之关联也删除
    on_delete=models.DO_NOTHING, # 删除关联数据,什么也不做
    on_delete=models.PROTECT, # 删除关联数据,引发错误ProtectedError
    # models.ForeignKey('关联表', on_delete=models.SET_NULL, blank=True, null=True)
    on_delete=models.SET_NULL, # 删除关联数据,与之关联的值设置为null（前提FK字段需要设置为可空,一对一同理）
    # models.ForeignKey('关联表', on_delete=models.SET_DEFAULT, default='默认值')
    on_delete=models.SET_DEFAULT, # 删除关联数据,与之关联的值设置为默认值（前提FK字段需要设置默认值,一对一同理）
    on_delete=models.SET, # 删除关联数据,
    a. 与之关联的值设置为指定值,设置：models.SET(值)
    b. 与之关联的值设置为可执行对象的返回值,设置：models.SET(可执行对象)
    '''
    goods_sn = models.CharField(max_length=50, unique=True, verbose_name="货号")
    name = models.CharField(max_length=100, verbose_name="名称")
    sold_num = models.IntegerField(default=0, verbose_name="销量")
    goods_num = models.IntegerField(default=0, verbose_name="库存")
    shop_price = models.FloatField(default=0, verbose_name="价格")
    goods_desc = UEditorField(verbose_name=u"内容", imagePath="goods/images/", width=1000, height=300, filePath="goods/files/", default='')
    cover = models.ImageField(upload_to="goods/images/", null=True, blank=True, verbose_name="封面图")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品", related_name="images")
    image = models.ImageField(upload_to="", verbose_name="图片", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name
