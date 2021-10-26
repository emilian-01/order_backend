from django.contrib import admin
from .models import OrderUnit, Order, Counter

# Register your models here.
admin.site.register(Order)
admin.site.register(Counter)
admin.site.register(OrderUnit)
