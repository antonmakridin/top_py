# #1
# words = ['apple', 'banana', 'cherry', 'eee', 'rwefwefwe']
# new = []
# for s in words:
#     if len(s) > 5:
#         new.append(s)
# print(new)


# #2
# m = input('введите пример ')
# if '+' in m:
#     m = m.split('+')
#     print(int(m[0]) + int(m[1]))
# elif '-' in m:
#     m = m.split('-')
#     print(int(m[0]) - int(m[1]))
# elif '*' in m:
#     m = m.split('*')
#     print(int(m[0]) * int(m[1]))
# elif '/' in m:
#     m = m.split('/')
#     if int(m[1]) == 0:
#         print('На ноль делить нельзя')
#     else:
#         print(int(m[0]) / int(m[1]))
# else:
#     print('Непонятное выражение')


# #3
# question = [['Столица Италии', 'Рим'], ['Длинная река в Египте', 'Нил'], ['Самый большой океан', 'Тихий']]
# for q in question:
#     otvet = True
#     o = input(q[0] + ' ').capitalize()
#     if o != q[1]:
#         otvet = False
#         print('Неправильный ответ')
#     else:
#         print('Правильный ответ')


# #4
# numbers = [12, 34, 2, 3, 46]
# max1 = numbers[0]
# for num in numbers:
#     if num > max1:
#         max = num
# print(max)


# #5
# # numbers = [12, 34, 2, 3, 46]
# from random import randint
# import time
# start_time = time.time()  # запоминаем время начала выполнения функции
# numbers = []
# for i in range(5000):
#     numbers.append(randint(1, 99))
# n = len(numbers)
# # for i in range(n-1):
# #     for j in range(n-1-i):
# #         if numbers[j] > numbers[j+1]:
# #             numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
# sort = []
# while numbers:
#     min1 = numbers[0]
#     for num in numbers:
#         if num < min1:
#             min1 = num
#     sort.append(min1)
#     numbers.remove(min1)
# print('отсортировал')
# end_time = time.time()  # запоминаем время окончания выполнения функции
# execution_time = end_time - start_time  # вычисляем время выполнения функции
# print(f"Время выполнения скрипта: {execution_time} секунд")


# #6
menu = ["Салат с курицей", "Веганский бургер", "Паста с грибами", "Бифштекс", "Рыбный суп"]
not_vegan_keywords = ["куриц", "бифштекс", "рыб", "мяс"]
for n in not_vegan_keywords:
    for m in menu:
        if m.count(n) != 0 or m.count(n.lower()) != 0 or m.count(n.capitalize()) != 0:
            menu.remove(m)
print(menu)


# #7
# # haystack = "sadbutsad"
# # needle = "sad"
# haystack = "leetcode"
# needle = "leeto"
# print(haystack.find(needle))


#8
