from django.shortcuts import render
from django.http import JsonResponse

from .wishlist import Wishlist

# Create your views here.


def wishlist_summary(request):
    wishlist = Wishlist(request)
    context = {'wishlist': wishlist}
    return render(request, 'templates/ecommerce/wishlist.html', context)


def wishlist_add(request):
    wishlist = Wishlist(request)
    if request.method == 'POST':
        product_id = request.POST.get('productid')
        wishlist.add(product_id)
        wishlist_qty = wishlist.__len__()
        return JsonResponse({'wishlistqty': wishlist_qty})


def wishlist_delete(request):
    wishlist = Wishlist(request)
    if request.method == 'POST':
        product_id = request.POST.get('productid')
        wishlist.delete(product_id)
        wishlist_qty = wishlist.__len__()
        return JsonResponse({'wishlistqty': wishlist_qty})
