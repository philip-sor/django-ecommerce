from shop.models import Product
from decimal import Decimal


class Basket:
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('basket')
        if 'basket' not in request.session:
            basket = self.session['basket'] = {}
        self.basket = basket

    def add(self, product, qty):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['qty'] += qty
        else:
            self.basket[product_id] = {}
            self.basket[product_id]['qty'] = qty
            self.basket[product_id]['price'] = str(product.price)
        self.session.modified = True

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]['product'] = product
        for item in basket.values():
            item['price'] = Decimal(item['product'].price)
            item['total_price'] = item['price'] * Decimal(item['qty'])
            yield item

    def __len__(self):
        return sum(int(product['qty']) for product in self.basket.values())

    def update(self, product_id, qty):
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.session.modified = True

    def basket_delete(self, product):
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.session.modified = True

    def get_total_price(self):
        delivery_price = 0
        if 'payment' in self.session:
            delivery_price = self.session['payment']['delivery_price']
        return sum(Decimal(item['qty']) * Decimal(item['price']) for item in self.basket.values()) \
               + Decimal(delivery_price)

    def get_subtotal_price(self):
        return sum(Decimal(item['qty']) * Decimal(item['price']) for item in self.basket.values())

    def get_delivery_price(self):
        if 'payment' in self.session:
            return self.session['payment']['delivery_price']
        else:
            return 0

    def get_address(self):
        if 'address' in self.session:
            return self.session['address']
        else:
            return None
