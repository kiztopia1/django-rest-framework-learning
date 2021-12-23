from django.urls import  path
from rest_framework import routers



from store.api_views  import  ProductList, ProductCreate, ReteriveUpdateDestroy

urlpatterns = [
    path('/', ProductList.as_view()),
    path('/add', ProductCreate.as_view() ),
    path('/<int:id>/', ReteriveUpdateDestroy.as_view() )
]