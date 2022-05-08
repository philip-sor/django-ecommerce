from django.urls import path
from . import views

app_name = 'basket'

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
    path('add/', views.basket_add, name='add'),
    path('update/', views.basket_update, name='update'),
    path('delete/', views.basket_delete, name='delete'),

]
