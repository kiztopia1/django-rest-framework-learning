from django.urls import  path
from rest_framework import routers



from store.api_views  import  ProductList

urlpatterns = [
    path('/', ProductList.as_view())
]