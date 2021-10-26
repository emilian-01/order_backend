from django.db import models


# Create your models here.

class ProductCategory(models.Model):
    class Meta:
        db_table = 'itw_product_category'
        verbose_name = 'product_category'
        verbose_name_plural = 'product_categories'

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        db_table = 'itw_product'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    name = models.CharField(max_length=50)
    default_price = models.FloatField()
    description = models.CharField(max_length=50)
    deleted = models.BinaryField(default=b'0')

    product_category = models.ManyToManyField(ProductCategory)

    def __str__(self):
        return self.name
