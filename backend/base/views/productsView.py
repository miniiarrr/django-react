from rest_framework.views import APIView
from rest_framework.response import Response
from base.models import Product
from base.serializers import ProductSerializer


class ProductsView(APIView):
    def get(self, request, product_id):
        product = Product.objects.filter(_id=product_id).first()

        if not product:
            message = {'detail': 'Product not found'}
            return Response(message, status=404)

        serialized_data = ProductSerializer(product).data

        return Response(serialized_data)


