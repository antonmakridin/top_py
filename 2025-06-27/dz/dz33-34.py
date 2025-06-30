#Задания в классе
# #1
# import json
# products = [{'name': 'яблоко', 'price': 100}, {'name': 'картошка', 'price': 50}, {'name': 'молоко', 'price': 200}]
# with open('2025-06-27\\dz\\z1.json', 'w', encoding='utf-8') as f:
#     json.dump(products, f, ensure_ascii=True, indent=4)


# #2
# import json
# with open('2025-06-27\\dz\\z2.json', 'w', encoding='utf-8') as f:
#     tovars = []
#     for _ in range(5):
#         name = input('Введи название товара: ')
#         price = int(input('Введи цену товара: '))
#         tovar = {
#             "name": name,
#             "price": price
#         }
#         tovars.append(tovar)
#     json.dump(tovars, f, ensure_ascii=True, indent=4)
# print('Молодец, добавил 5 товаров\n')


# #3
# import json
# while True:
#     do = int(input('\nВыберите действие: \nДобавить товар - 1\nПосмотреть товары - 2\nВыход - 3\n'))
#     if do == 1:
#         with open('2025-06-27\\dz\\z3.json', encoding='utf-8') as f:
#             tovars = json.load(f)
#         name = input('Введи название товара: ')
#         for w in tovars:
#             if name == w['name']:
#                 print('Такой товар уже есть')
#                 break
#         else:
#             price = int(input('Введи цену товара: '))
#             tovar = {
#                 "name": name,
#                 "price": price
#             }
#             tovars.append(tovar)
#             with open('2025-06-27\\dz\\z3.json', 'w', encoding='utf-8') as f:
#                 json.dump(tovars, f, ensure_ascii=True, indent=4)
#             print('Товар добавлен!\n')
#     elif do == 2:
#         with open('2025-06-27\\dz\\z3.json', 'r', encoding='utf-8') as f:
#             data = json.load(f)
#             print('\nСписок товаров:')
#             for d in data:
#                 print(d['name'], d['price'])
#     elif do == 3:
#         break


#Задания домашней работы
# #1
# import json
# data = [{'country': 'Russia', 'capital': 'Moscow'},
#  {'country': 'USA', 'capital': 'Washington'}]
# with open('2025-06-27\\dz\\dz1.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=True, indent=4)

# #2
# import json
# with open('2025-06-27\\dz\\dz1.json', encoding='utf-8') as f:
#     countries = json.load(f)
# name = input('Введи название страны: ')
# cap = input('Введи название столицы: ')
# country = {
#     "country": name,
#     "capital": cap
# }
# countries.append(country)
# with open('2025-06-27\\dz\\dz1.json', 'w', encoding='utf-8') as f:
#     json.dump(countries, f, ensure_ascii=True, indent=4)
# print('Страна добавлена!\n')

# #3
import json
print('Викторина')
right = 0
not_right = []
with open('2025-06-27\\dz\\dz1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    for d in data:
        print('Столица страны', d['country'])
        name = input(f'Ваш ответ: ')
        if name == d['capital']:
            right += 1
        else:
            d.update({'your_answer': name})
            not_right.append(d)
print(f'Правильных ответов: {right}')
print('Неправильные ответы:')
for item in not_right:
    print(f"Страна: {item['country']}, Ваш ответ: {item['your_answer']}, правильный ответ: {item['capital']}")