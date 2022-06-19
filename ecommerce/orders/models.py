from django.db import models
from django.conf import settings

from shop.models import Product
# Create your models here.


class Order(models.Model):
    order_id = models.CharField(max_length=30,)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.DO_NOTHING, default=None, null=True, blank=True)
    full_name = models.CharField(max_length=255, null=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    post_office_name = models.CharField(max_length=40, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    order_key = models.CharField(max_length=200)
    price_total = models.FloatField()
    is_payed = models.BooleanField(default=False)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

