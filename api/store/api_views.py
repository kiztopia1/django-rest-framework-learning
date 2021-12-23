from rest_framework.generics import ListAPIView
from store.serializer import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from store.models import Product


class ProductsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('id', )
    search_fields = ('name', 'price') 
    pagination_class = ProductsPagination

