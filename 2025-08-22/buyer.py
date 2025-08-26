class Customer:
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.total_purchases = 0
        self.purchase_history = []
    
    def __str__(self):
        return f"Пользователь {self.name}: денег - {self.money} руб., покупок - {self.total_purchases}"
    
    def show_history(self):
        # история покупок
        if not self.purchase_history:
            print("История покупок пуста")
            return
        
        print(f"\nИстория покупок пользователя {self.name}:")
        for i, purchase in enumerate(self.purchase_history, 1):
            print(f"{i}. {purchase['product']} - {purchase['quantity']} шт. за {purchase['total_cost']} руб.")


class Shop:
    def __init__(self):
        self.database = []
        self.total_sales = 0
        self.total_receipts = 0
    
    def add_product(self, name, price, count):
        # добавление продукта в БД
        for product in self.database:
            if product["name"] == name:
                print(f"Продукт '{name}' уже существует! Используйте add_product_count() для увеличения количества.")
                return False
        
        product = {
            "name": name,
            "price": price,
            "count": count
        }
        self.database.append(product)
        print(f"Добавлен продукт: {name} - {price} руб. (в наличии: {count} шт.)")
        return True
    
    def delete_product(self, name):
        # удаление продукта из БД
        for i, product in enumerate(self.database):
            if product["name"] == name:
                deleted_product = self.database.pop(i)
                print(f"Товар '{name}' удален из базы данных")
                return deleted_product
        
        print(f"Товар '{name}' не найден в базе данных!")
        return None
    
    def add_product_count(self, name, count):
        # увеличение количества товара на указанное значение
        for product in self.database:
            if product["name"] == name:
                product["count"] += count
                print(f"Количество товара '{name}' увеличено на {count} шт. Теперь в наличии: {product['count']} шт.")
                return True
        
        print(f"Товар '{name}' не найден в базе данных! Сначала добавьте его с помощью add_product()")
        return False
    
    def buy(self, customer):
        #  покупка товара через меню
        if not self.database:
            print("В магазине нет товаров для покупки!")
            return False
        
        print(f"\n=== МЕНЮ ПОКУПОК для {customer.name} ===")
        print(f"Ваш баланс: {customer.money} руб.")
        self.show_products()
        
        while True:
            try:
                choice = input("Выберите товар (введите номер или название, или 'выход' для отмены): ").strip()
                
                if choice.lower() in ['выход', 'exit', 'quit', 'отмена']:
                    print("Покупка отменена")
                    return False
                
                # Пытаемся найти товар по номеру
                if choice.isdigit():
                    product_num = int(choice)
                    if 1 <= product_num <= len(self.database):
                        selected_product = self.database[product_num - 1]
                        break
                    else:
                        print("Неверный номер товара! Попробуйте снова.")
                        continue
                
                # Ищем товар по названию
                found_products = []
                for product in self.database:
                    if product["name"].lower() == choice.lower():
                        found_products.append(product)
                
                if len(found_products) == 1:
                    selected_product = found_products[0]
                    break
                elif len(found_products) > 1:
                    print("Найдено несколько товаров с таким названием:")
                    for i, product in enumerate(found_products, 1):
                        print(f"{i}. {product['name']} - {product['price']} руб.")
                    continue
                else:
                    print("Товар не найден! Попробуйте снова.")
                    
            except ValueError:
                print("Пожалуйста, введите корректный номер или название товара.")
        
        # Выбор количества
        while True:
            try:
                quantity = input(f"Сколько '{selected_product['name']}' вы хотите купить? (доступно: {selected_product['count']} шт.): ").strip()
                
                if quantity.lower() in ['выход', 'exit', 'quit', 'отмена']:
                    print("Покупка отменена")
                    return False
                
                quantity = int(quantity)
                if quantity <= 0:
                    print("Количество должно быть положительным числом!")
                    continue
                
                if quantity > selected_product["count"]:
                    print(f"Недостаточно товара! Доступно только {selected_product['count']} шт.")
                    continue
                
                break
                    
            except ValueError:
                print("Пожалуйста, введите число!")
        
        # совершаем покупку
        total_cost = selected_product["price"] * quantity
        
        if customer.money < total_cost:
            print(f"Недостаточно денег! Нужно {total_cost} руб., а у вас {customer.money} руб.")
            return False
        
        # подтверждение покупку
        confirm = input(f"Подтвердите покупку: {quantity} шт. '{selected_product['name']}' за {total_cost} руб. (да/нет): ").strip().lower()
        if confirm not in ['да', 'yes', 'y', 'д']:
            print("Покупка отменена")
            return False
        
        # выполняем покупку
        selected_product["count"] -= quantity
        customer.money -= total_cost
        customer.total_purchases += 1
        customer.purchase_history.append({
            'product': selected_product['name'],
            'quantity': quantity,
            'price_per_unit': selected_product['price'],
            'total_cost': total_cost
        })
        
        self.total_sales += total_cost
        self.total_receipts += 1
        
        print(f"Покупка успешна! Куплено {quantity} шт. '{selected_product['name']}' за {total_cost} руб.")
        print(f"Остаток на складе: {selected_product['count']} шт.")
        print(f"Ваш остаток: {customer.money} руб.")
        
        return True
    
    def get_info(self):
        # итоговая сумма покупок и количество чеков
        return {
            "total_sales": self.total_sales,
            "total_receipts": self.total_receipts,
            "total_products": len(self.database)
        }
    
    def show_products(self):
        # отобразить доступные продукты
        print("\nДоступные продукты:")
        if not self.database:
            print("В магазине нет товаров!")
            return
        
        for i, product in enumerate(self.database, 1):
            print(f"{i}. {product['name']} - {product['price']} руб. (в наличии: {product['count']} шт.)")
        print()


# Главное меню программы
def main_menu():
    shop = Shop()
    
    # Добавляем тестовые товары
    shop.add_product("Молоко", 80, 10)
    shop.add_product("Хлеб", 45, 15)
    shop.add_product("Сыр", 200, 8)
    shop.add_product("Яйца", 75, 20)
    shop.add_product("Масло", 220, 12)
    
    # Создаем пользователя
    customer_name = input("Введите ваше имя: ").strip()
    customer_money = 0
    while True:
        try:
            customer_money = float(input("Введите начальный баланс: "))
            if customer_money < 0:
                print("Баланс не может быть отрицательным!")
                continue
            break
        except ValueError:
            print("Пожалуйста, введите число!")
    
    customer = Customer(customer_name, customer_money)
    
    while True:
        print("\n" + "="*50)
        print("ГЛАВНОЕ МЕНЮ МАГАЗИНА")
        print("="*50)
        print(f"Пользователь: {customer.name}")
        print(f"Баланс: {customer.money} руб.")
        print("1. Показать товары")
        print("2. Купить товар")
        print("3. История покупок")
        print("4. Статистика магазина")
        print("5. Выход")
        print("="*50)
        
        choice = input("Выберите действие (1-5): ").strip()
        
        if choice == "1":
            shop.show_products()
        
        elif choice == "2":
            shop.buy(customer)
        
        elif choice == "3":
            customer.show_history()
        
        elif choice == "4":
            info = shop.get_info()
            print(f"\nСтатистика магазина:")
            print(f"Общая сумма продаж: {info['total_sales']} руб.")
            print(f"Количество чеков: {info['total_receipts']}")
            print(f"Количество товаров: {info['total_products']}")
        
        elif choice == "5":
            print("Спасибо за покупки! До свидания!")
            break
        
        else:
            print("Неверный выбор! Попробуйте снова.")
        
        input("\nНажмите Enter для продолжения...")


# Запуск программы
main_menu()
