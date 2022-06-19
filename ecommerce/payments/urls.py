from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    path('delivery/', views.delivery_choices, name='delivery_choices'),
    path('update-delivery/', views.change_delivery, name='update_delivery'),
    path('address-choices/', views.address_choices, name='address_choices'),
    path('checkout/', views.checkout, name='checkout'),

    path('payment-complete/', views.payment_complete, name='payment_complete'),
    path('payment-successful/', views.payment_successful, name='payment_successful'),

]
