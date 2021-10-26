from rest_framework import serializers
from .models import Order, Counter, OrderUnit


class OderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OderUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUnit
        fields = '__all__'


class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = '__all__'
