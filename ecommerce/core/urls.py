from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path(r'', views.home, name='home'),
    path(r'all/', views.show_all, name='all'),
    path(r'<str:pk>', views.detail_page, name='detail_page')
]
