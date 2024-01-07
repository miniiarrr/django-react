from base.products import products
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductsView(APIView):
    def get(self, request, product_id):
        for product in products:
            if product['_id'] == product_id:
                return Response(product)

        message = {'detail': 'Product not found'}
        return Response(message, status=404)


