import json
from decimal import Decimal

from django.shortcuts import render, redirect
from django.http import JsonResponse

from basket.basket import Basket
from shop.models import Product
from orders.models import Order, OrderItem
from .models import Delivery
from .forms import AddressForm

# paypal
from .paypal import PayPalClient
from paypalcheckoutsdk.orders import OrdersGetRequest

# Create your views here.


def delivery_choices(request):
    if Basket(request).__len__() == 0:
        return redirect('basket:basket_summary')
    delivery_options = Delivery.objects.filter(is_active=True)
    context = {
        'delivery_options': delivery_options
    }
    return render(request, 'templates/ecommerce/payments/delivery_choices.html', context)


def change_delivery(request):
    session = request.session
    basket = Basket(request)
    if request.method == 'POST':
        delivery_id = str(request.POST.get('deliveryid'))
        delivery_price = str(Delivery.objects.get(id=delivery_id).delivery_price)
        if 'payment' not in session:
            session['payment'] = {'delivery_id': delivery_id,
                                  'delivery_price': delivery_price}
        else:
            session['payment']['delivery_id'] = delivery_id
            session['payment']['delivery_price'] = delivery_price
        session.modified = True
        total_price = basket.get_total_price()
        return JsonResponse({'delivery_price': delivery_price,
                             'total_price': total_price})


def address_choices(request):
    session = request.session
    context = {'form': AddressForm}
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            session['address'] = {'address1': request.POST.get('address1'),
                                  'address2': request.POST.get('address2'),
                                  'town_city': request.POST.get('town_city'),
                                  'postcode': request.POST.get('postcode'),
                                  'post_office_name': request.POST.get('post_office_name'),
                                  'email': request.POST.get('email'),
                                  'phone_number': request.POST.get('phone_number'),
                                  }
        context = {'form': form}
    return render(request, 'templates/ecommerce/payments/address_choices.html', context)


def checkout(request):
    context = {}
    return render(request, 'templates/ecommerce/payments/checkout.html', context)


def payment_successful(request):
    PPClient = PayPalClient()
    body = json.loads(request.body)
    data = body['orderID']
    requestorder = OrdersGetRequest(data)
    response = PPClient.client.execute(requestorder)
    print(requestorder)
    print(response)
    user = None
    if request.user.is_authenticated():
        user = request.user
    total_paid = response.result.purchase_units[0].amount.value

    basket = Basket(request)
    order = Order.objects.create(
        customer=user,
        full_name=response.result.purchase_units[0].shipping.name.full_name,
        email=response.result.payer.email,
        address1=response.result.purchase_units[0].shipping.address.address_line_1,
        address2=response.result.purchase_units[0].shipping.address.admin_area_2,
        post_code=response.result.purchase_units[0].shipping.address.postal_code,
        price_total=response.result.purchase_units[0].amount.value,
        order_key=response.result.id,
        is_payed=True,
    )
    order_id = order.pk

    for item in basket:
        OrderItem.objects.create(order=order, product=item["product"], price=item["price"], quantity=item["qty"])

    return JsonResponse("Payment completed!", safe=False)


def payment_complete(request):
    return redirect('shop:all')

