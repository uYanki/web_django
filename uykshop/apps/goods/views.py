
from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework.pagination import PageNumberPagination

from rest_framework import viewsets


from .models import Goods
# Create your views here.


'''
class GoodsListView(APIView):
    # http://127.0.0.1:8000/goods/?format=api
    # http://127.0.0.1:8000/goods/?format=json
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        goods_serializer = GoodsSerializer(goods, many=True)
        return Response(goods_serializer.data)

    # def post(self, request, format=None):
    #     goods_serializer = GoodsSerializer(data=request.data)
    #     if goods_serializer.is_valid():
    #         goods_serializer.save()
    #         return Response(goods_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(goods_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''


'''
class GoodsListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Goods.objects.all()[:10]
    serializer_class = GoodsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
'''


class GoodsListView2(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    pass


class GoodsPagination(PageNumberPagination):
    # 自定分页器
    page_size = 2
    page_size_query_param = "page_size"
    page_query_param = "p"
    max_page_size = 10


class GoodsListView(generics.ListAPIView):
    # 更简单 可省去get，具体看 generics 有什么可继承的class
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    # http://localhost:8000/goods/?p=1&page_size=20


class GoodsListViewSet(viewsets.ModelViewSet):
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
