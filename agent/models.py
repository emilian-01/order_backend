from django.db import models


# Create your models here.

class Customer(models.Model):
    class Meta:
        db_table = 'itw_customer'
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(max_length=50)
    deleted = models.BinaryField(default=b'0')

    def __str__(self):
        return self.first_name
