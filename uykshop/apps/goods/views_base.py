import json

from django.views.generic.base import View
from django.core import serializers  # Model(mult) to Json
from django.forms.models import model_to_dict  # Model(one) to Dict
from django.http import HttpResponse, JsonResponse

from .models import Goods


class GoodsListView(View):
    def get(self, request):
        goods = Goods.objects.all()[:10]  # 获取数据
        json_data = serializers.serialize('json', goods)  # 序列化JSON
        # return JsonResponse(json_data, safe=False)  # 响应请求
        return HttpResponse(json_data, content_type="application/json")

        # json_data = []
        # for good in goods:
        #     json_dict = model_to_dict(good) # 模型转字典
        #     json_data.append(json_dict)
