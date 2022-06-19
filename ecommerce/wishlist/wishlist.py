from shop.models import Product
from decimal import Decimal


class Wishlist:
    def __init__(self, request):
        self.session = request.session
        wishlist = self.session.get('wishlist')
        if 'wishlist' not in self.session:
            wishlist = self.session['wishlist'] = {}
        self.wishlist = wishlist

    def add(self, product_id):
        product = Product.objects.get(id=str(product_id))
        if str(product.id) not in self.wishlist:
            self.wishlist[str(product.id)] = {'price': str(product.price)}
            self.session.modified = True

    def delete(self, product_id):
        if str(product_id) in self.wishlist:
            del self.wishlist[str(product_id)]
            self.session.modified = True

    def __iter__(self):
        product_ids = self.wishlist.keys()
        products = Product.objects.filter(id__in=product_ids)
        wishlist = self.wishlist.copy()
        for product in products:
            wishlist[str(product.id)]['product'] = product
        for item in wishlist.values():
            item['price'] = Decimal(item['product'].price)
            yield item

    def __len__(self):
        return len(self.wishlist)
