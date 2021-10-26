from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import OderSerializer, OderUnitSerializer, CounterSerializer
from .models import Order, OrderUnit, Counter


# Create your views here.

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OderSerializer
    queryset = Order.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class OrderUnitViewSet(viewsets.ModelViewSet):
    serializer_class = OderUnitSerializer
    queryset = OrderUnit.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class CounterViewSet(viewsets.ModelViewSet):
    serializer_class = CounterSerializer
    queryset = Counter.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
