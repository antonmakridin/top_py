import json

class Shop():

    def __init__(self):
        self.default = {'Молоко': 10, 'Колбаса': 20}
        self.listBuy = {}
        self.summaItog = 0

    def buy(self, product):

        if len(product) == 0:
            print('Не указано название товара')
        
        if product not in self.default.keys():
            print('Нет такого товара в списке покупок')
        else:
            price = self.default.get(product)
            self.listBuy[product] = price
            print(f'купили {product}')

    def add_product(self, product, price):
        if len(product) == 0:
            print('Не указано название товара')
        
        if product not in self.default.keys():
            self.default[product] = price
            print(f'Товары обновлены')
        else:
            print('Такой товар уже есть')

    def get_info(self):
        for p in self.listBuy.values():
            self.summaItog += p
        print(f'Общая сумма: {self.summaItog}')
        print(f'Чеки: {len(self.listBuy)}')

s = Shop()
s.buy('Молоко')
s.buy('Яйца')
s.buy('Колбаса')
s.add_product('Яйца', 100)
s.buy('Яйца')
s.get_info()