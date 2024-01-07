from django.urls import path
from base.views.routesView import RoutesView
from base.views.listProductsView import ListProductsView

urlpatterns = [
    path('', RoutesView.as_view(), name='routes'),
    path('products/', ListProductsView.as_view(), name='products'),

]
