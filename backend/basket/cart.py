from django.contrib.sessions.models import Session
from decimal import Decimal
from pprint import pprint
from catalog.models import ProductProxy


class Cart():

    def __init__(self, request) -> None:
        self.session = request.session
        cart = self.session.get('session_key')

        if not cart:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def __len__(self):
        return sum(item['qty'] for item in self.cart.values())

    def __iter__(self):
        product_ids = self.cart.keys()
        products = ProductProxy.published.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item
        
    def add(self, product, quantity):
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {'qty': quantity, 'price': str(product.price)}
        
        self.cart[product_id]['qty'] = quantity

        self.session.modified = True

    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def clean_users_session(self):
        for product_id, _ in list(self.cart.items()):
            del self.cart[product_id]
            self.session.modified = True

    def update(self, product, quantity):
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = quantity
            self.session.modified = True

    def check_message_Telegram(self, sendMessage):
        message = ''
        for item in sendMessage:
            try:
                message += ' '.join(['Наименование:\n' + sendMessage[item]['product'],'Количество:', str(sendMessage[item]['qty']),'Цена:', sendMessage[item]['price']+ '\n'])
                message += f'Общая стоимость: <b>{self.get_total_price()} руб.\n</b>'
            except Exception as ex:
                print('Ошибка', ex)
        return message 


    def sendMessage(self):
        product_ids = self.cart.keys()
        products = ProductProxy.published.filter(id__in=product_ids)
        cart = self.cart.copy()
        sendMessage = self.cart.copy()
        for product in products:
            sendMessage[str(product.id)]['product'] = product.name
        return self.check_message_Telegram(sendMessage)

    def get_total_price(self):
        return sum(Decimal(item['price'])* item['qty'] for item in self.cart.values())