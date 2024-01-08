from rest_framework.views import APIView
from rest_framework.response import Response
from base.models import Product
from base.serializers import ProductSerializer


class ListProductsView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()

        serialized_data = ProductSerializer(products, many=True).data

        return Response(serialized_data)
