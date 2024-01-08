from rest_framework.serializers import ModelSerializer
from base.models import *


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
