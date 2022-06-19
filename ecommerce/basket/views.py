from django.shortcuts import render
from django.http import JsonResponse

from .basket import Basket
from shop.models import Product

# from ecommerce.shop.models import Product
# Create your views here.


def basket_summary(request):
    basket = Basket(request)
    context = {'basket': basket}
    return render(request, 'templates/ecommerce/basket.html', context)


def basket_add(request):
    basket = Basket(request)
    if request.method == 'POST':
        product_id = request.POST.get('productid')
        qty = int(request.POST.get('qty'))
        product = Product.objects.get(id=product_id)
        basket.add(product=product, qty=qty)

        basketqty = basket.__len__()
        return JsonResponse({'qty': basketqty})


def basket_update(request):
    basket = Basket(request)
    if request.method == 'POST':
        product_id = request.POST.get('productid')
        qty = request.POST.get('qty')
        basket.update(product_id=product_id, qty=qty)

        subtotal = basket.get_subtotal_price()
        basketqty = basket.__len__()
        return JsonResponse({'subtotal': subtotal, 'basketqty': basketqty})


def basket_delete(request):
    basket = Basket(request)
    if request.method == "POST":
        product_id = request.POST.get('productid')
        product = Product.objects.get(id=product_id)
        basket.basket_delete(product)
        subtotal = basket.get_subtotal_price()
        basketqty = basket.__len__()
        return JsonResponse({'subtotal': subtotal, 'basketqty': basketqty})
