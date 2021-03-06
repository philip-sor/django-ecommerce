from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    path('basket/', include('basket.urls', namespace='basket')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('wishlist/', include('wishlist.urls', namespace='wishlist')),
    path('payments/', include('payments.urls', namespace='payments')),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
