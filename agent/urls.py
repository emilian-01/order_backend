from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, UserViewSet

router = DefaultRouter()
router.register('customer', CustomerViewSet, basename='customer')
router.register('user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
