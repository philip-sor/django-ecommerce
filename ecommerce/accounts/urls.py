from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register_account, name='register'),
    path('login/', views.login_account, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/accounts/login'), name='logout'),

    path('activate/<slug:uid64>/<slug:token>', views.account_activate, name='activate')
]
