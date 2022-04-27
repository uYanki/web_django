

from rest_framework import serializers
from .models import Goods, GoodsCategory

# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, required=True)
#     sold_num = serializers.IntegerField(default=0)
#     cover = serializers.ImageField()  # FileField、ImageField会自动在头部添加 settings.MEDIA_URL （django自带的不会加）

#     def create(self, validated_data):
#         return Goods.objects.create(**validated_data)


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    # 比上面的GoodsSerializer更简单
    category = GoodsCategorySerializer()  # 序列化嵌套（django不能直接做到的）

    class Meta:
        model = Goods
        # fields = ('name', 'sold_num', 'cover', 'add_time')
        fields = "__all__"
