from django.urls import path
from base.views.routesView import RoutesView
from base.views.listProductsView import ListProductsView
from base.views.productsView import ProductsView

urlpatterns = [
    path('', RoutesView.as_view(), name='routes'),
    path('products/', ListProductsView.as_view(), name='products'),
    path('products/<str:product_id>', ProductsView.as_view(), name='product'),

]
