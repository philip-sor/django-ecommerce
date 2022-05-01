import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30, unique=True)

    class Meta:
        pass

    def __str__(self):
        return self.category

    def get_absolute_url(self):
        pass


class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/', default='products/default.jpg')
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    slug = models.SlugField(max_length=120, unique=True)
    category = models.ForeignKey(Category, default='None', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated', '-created')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:detail_page', args=[self.slug, ])
