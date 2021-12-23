from django.db import models
from rest_framework import serializers

from store.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ( 'id', 'name', 'price', )

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     return data