# #1
# a = 4
# b = 8
# print(f'Площадь прямоугольника со сторонами {a} и {b} равен {a * b}')


# #2
# s = int(input('Укажите расстояние в километрах: '))
# v = int(input('Укажите скорость в км/ч: '))
# print(f'Вам потребуется времени: {s / v} час.')


# #3
# score = int(input("Введите количество набранных баллов (от 0 до 100): "))
# if 80 <= score <= 100:
#     print("отлично")
# elif 60 <= score <= 79:
#     print("хорошо")
# elif 40 <= score <= 59:
#     print("нормально")
# elif 0 <= score < 40:
#     print("ну такое")
# else:
#     print("Ошибка: введите число от 0 до 100")


# #4
# for number in range(1, 11):
#     print(number)


# #5
# s = 'asdf1f3aak4ff2fkj2dd3dd4'
# count = 0
# for char in s:
#     if char.isdigit():
#         count += 1
# print(count)


# #6
# s1 = 'пкрйизвтедтe e'
# s2 = 'кзадкm rдыеьлжа'
# itog = s1 + s2
# result = ""
# for i in range(0, len(itog), 2):
#     result += itog[i]
# print(result)


# #7
# l = ['1', 'a', 'b', '2', '5', 'sdf', '12']
# numbers = []
# for item in l:
#     if item.isdigit():
#         numbers.append(int(item))
# summa = 0
# for num in numbers:
#     summa += num
# print("Числа:", numbers)
# print("Сумма:", summa)


# #8
# names = []
# for _ in range(5):
#     name = input('Введите имя пользователя: ')
#     if names.count(name):
#         print('Такое имя уже есть! Введи другое!')
#     else:
#         names.append(name)
# print(names)


# #9
# names = []
# while len(names) < 4:
#     name = input('Введите имя пользователя: ')
#     if names.count(name):
#         print('Такое имя уже есть! Введи другое!')
#     else:
#         names.append(name)
# print(names)


# #10 Дано два списка. Сложите их и найдите максимум, не пользуясь методом sorted() и max().
# l1 = [1,45,3,2,9,1]
# l2 = [4,3,2,98,1]
# l3 = l1 + l2
# maximum = l3[0]
# for num in l3:
#     if num > maximum:
#         maximum = num
# print('Максимальное значение равно', maximum)


# #11 Дан словарь с ценам на продукты. Напишите программу, которая спрашивает у пользователя действие, которое надо сделать
# prod = {'чашка': 500, 'апельсины': 120, 'ложка': 100}
# while True:
#     do = int(input('Выберите действие: \nДобавить новый товар - 1\nПолучить цену товара - 2\nВыход - 3\n'))
#     if do == 1:
#         tovar = input('Введите название товара: ')
#         price = int(input('Введите стоимость товара'))
#         prod[tovar.lower()] = price
#     elif do == 2:
#         user  = input('Введите название товара: ')
#         if user.lower() in prod:
#             print('Стоимость товара', user, 'составляет', prod[user.lower()])
#         else:
#             print('Такого товара нет')
#     elif do == 3:
#         print('До свидания!')
#         break


# #12+1 Дан словарь, создайте новый словарь, в котором будут все продукты, которые дешевле 300 рублей.
# prod = {'чашка': 500, 'апельсины': 120, 'ложка': 100}
# prod2 = {}
# for product, price in prod.items():
#     if price < 300:
#         prod2[product] = price
# print(prod2)


# #14 Дано два спика. Превратите их во множества. Найдите числа, которые есть и там и там.
# l1 = [1, 45, 3, 2, 1, 54, 8]
# l2 = [8, 1, 43, 45]
# # dubl_numbers = []
# # for n in l1:
# #     if n in l2 and n not in dubl_numbers:
# #         dubl_numbers.append(n)
# # print(dubl_numbers)
# #или
# mn1 = set(l1)
# mn2 = set(l2)
# dubl_numbers = mn1 & mn2
# print(dubl_numbers)


# #15 Дан кортеж из паролей. Напишите программу, которая спрашивает у пользователя имя, потом пароль. Если пароль есть в кортеже, добавьте пользователя в список. Программа должна работать, пока длина списка меньше 3.
# passw = ('asdf', '1234', 'lol')
# users = []
# while len(users) < 3:
#     name = input("Введите имя: ")
#     password = input("Введите пароль: ")
#     if password in passw:
#         users.append(name)
#         print(f"Пользователь {name} добавлен!")
#     else:
#         print("Неверный пароль. Введите заново.")
# print("\nПеречень пользователей:", users)


#16 Фраза зашифрована шифром Цезаря со смещением 5
str = "тньйзу цйёй, жуч вчу рйзпед иусеэпе"
decod = []
alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
for i in range(len(str)):
    if str[i] == " ":
        decod.append(' ')
    elif str[i] == ",":
        decod.append(',')
    else:
        decod_num = alph.index(str[i]) - 5
        if decod_num > 0:
            decod.append(alph[decod_num])
        elif decod_num < 0:
            decod_num = decod_num + len(alph)
            decod.append(alph[decod_num])
        elif decod_num == 0:
            decod.append(alph[0])
        else:
            print('ошибка')
print(decod)