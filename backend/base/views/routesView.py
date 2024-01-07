from django.views import View
from django.http import JsonResponse


class RoutesView(View):
    def get(self, request, *args, **kwargs):
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
        return JsonResponse(routes, safe=False)
