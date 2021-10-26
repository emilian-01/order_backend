from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, ProductCategoryViewSet

router = DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('category', ProductCategoryViewSet, basename='product-category')

urlpatterns = [
    path('', include(router.urls)),
]
