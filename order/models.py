from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from agent.models import Customer
from product.models import Product


# Create your models here.

class Order(models.Model):
    class Meta:
        db_table = 'itw_order'
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    code = models.IntegerField()
    code_year = models.IntegerField(default=timezone.now().year)
    date_registered = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.code)


class Counter(models.Model):
    class Meta:
        db_table = 'itw_counter'
        verbose_name = 'counter'
        verbose_name_plural = 'counters'

    name = models.CharField(max_length=10)
    value = models.IntegerField()

    def __str__(self):
        return self.name


class OrderUnit(models.Model):
    class Meta:
        db_table = 'itw_order_unit'
        verbose_name = 'order_unit'
        verbose_name_plural = 'order_units'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_units')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_units')
    amount = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return str(self.id)
