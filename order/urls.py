from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet, OrderUnitViewSet, CounterViewSet

router = DefaultRouter()
router.register('order', OrderViewSet, basename='order')
router.register('orderunit', OrderUnitViewSet, basename='order')
router.register('counter', CounterViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
