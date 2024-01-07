from django.urls import path
from base.views.routesView import RoutesView

urlpatterns = [
    path('', RoutesView.as_view(), name='routes'),
]
