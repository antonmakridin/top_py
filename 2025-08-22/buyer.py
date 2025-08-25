import json

class Shop:

    def __init__(self):
        # self.name = name
        # self.money = money
        self.default = []
        self.listBuy = []
        self.summaItog = 0

    def buy(self, name):

        if len(name) == 0:
            print('Не указано название товара')
        
        for w in self.default:
            if name == w['name']:
                tovar = {
                    "name": w['name'],
                    "price": w['price'],
                    "count": 1
                }
                self.listBuy.append(tovar)

    def add_product(self, name, price, count=None):
        if len(name) == 0:
            print('Не указано название товара')
        if price == 0:
            print('Не указана цена')
        
        for w in self.default:
            if name == w['name']:
                print('Такой товар уже есть в списке покупок')
        else:
            tovar = {
                "name": name,
                "price": price,
                "count": (count if count else 1)
            }
            self.default.append(tovar)
            print('Товар добавлен')
    
    def info(self):
        print(self.default)
        print(self.listBuy)

    def get_info(self):
        for p in self.listBuy.values():
            self.summaItog += p
        print(f'Общая сумма: {self.summaItog}')
        print(f'Чеки: {len(self.listBuy)}')


class Customer:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.listdefault = Shop()

    def buy_product(self):
        print(self.listdefault.info)


s = Shop()
# s.buy('Молоко')
# s.buy('Яйца')
# s.buy('Колбаса')
s.add_product('Яйца', 100, 5)
s.add_product('Хлеб', 100)
s.buy('Яйца')
# s.buy('Яйца')
s.info()

customer = Customer('Иван', 250)