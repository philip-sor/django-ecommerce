from django.db import models
# Create your models here.


class Delivery(models.Model):
    DELIVERY_CHOICES = [
        ("IS", "In Store"),
        ("HD", "Home Delivery"),
        ("DD", "Digital Delivery"),
    ]

    delivery_name = models.CharField(max_length=100)
    delivery_timeframe = models.CharField(max_length=15)
    delivery_window = models.CharField(max_length=20)
    delivery_price = models.DecimalField(max_digits=5, decimal_places=2)
    delivery_method = models.CharField(DELIVERY_CHOICES, max_length=255,)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.delivery_name
