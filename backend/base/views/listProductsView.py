from base.products import products
from rest_framework.views import APIView
from rest_framework.response import Response


class ListProductsView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(products)
