from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

from .models import Product

# Create your views here.


def home(request):
    return render(request, 'templates/home.html')


def show_all(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'templates/ecommerce/all.html', context)


def detail_page(request, pk):
    product = get_object_or_404(Product, slug=pk, in_stock=True)
    context = {'product': product}
    return render(request, 'templates/ecommerce/single.html', context)
