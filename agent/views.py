from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from .serializers import CustomerSerializer, UserSerializer
from .models import Customer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Customer.objects.all()
        deleted = self.request.query_params.get('deleted', b'0')
        if deleted is not None:
            queryset = queryset.filter(deleted=deleted)
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.deleted = b'1'
        instance.save()


# class IsSuperUser(IsAdminUser):
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_superuser)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)


# username          password
# admin             pass
# landi             l1a2n3d4i5
# beni              b1e2n3i4