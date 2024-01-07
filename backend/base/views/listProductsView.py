from rest_framework.views import APIView
from rest_framework.response import Response
from base.models import Product


class ListProductsView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()

        return Response(products)
