from django.views import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response


class RoutesView(APIView):
    def get(self, request):
        routes = [
            '/api/products',

            '/api/products/create',
            '/api/products/upload',
            '/api/products/top',

            '/api/products/<id>/reviews',
            '/api/products/<id>',

            '/api/products/delete/<id>',
            '/api/products/update/<id>',
        ]
        return Response(routes)
