from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, response

from .basket import Basket
from core.models import Product

# from ecommerce.core.models import Product
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

