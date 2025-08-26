class Shop:

    def __init__(self):
        self.all_sum = 0
        self.count_products = 0
        self.products = [{'name': 'Хлеб', 'price': 50, 'count': 2},
                         {'name': 'Молоко', 'price': 60, 'count': 1}]

    def buy(self, product_name, user):
        # ищем продукт по имнеи
        print(f'В магазине: {user}')
        for product in self.products:
            if product['name'] == product_name:
                if product['count'] > 0:
                    print(f'Попытка купить {product_name}')
                    if user.balance > product['price']:
                        print(f'Купили: {product_name} ')
                        self.all_sum += product['price']
                        self.count_products += 1
                        product['count'] -= 1
                        user.balance -= product['price']
                        print(f'Купили {product_name}. Баланс {user.balance}')
                    else:
                        print('Не хватает денег')
                else:
                    print('товар закончился...')
                break
        else:
            print('такого товара нет')

    def add_products(self, name, price, count=1):
        product = {'name': name, 'price': price, 'count': count}
        self.products.append(product)
        print(f'Добавили товар: {name}')

    def get_info(self):
        print(f'Сумма всех покупок: {self.all_sum} Количество: {self.count_products}')


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        
    def __str__(self):
        return self.name

user1 = User('Иван', 100)
user2 = User('Алиса', 80)
shop = Shop()
shop.buy('Хлеб', user1)