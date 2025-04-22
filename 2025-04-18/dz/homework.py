# Задание 1 ----------------------------------------------
# name = input('Введите имя: ')
# if name:
#     # /////////Вариант for
#     # for i in range(5):
#         # print(f'Привет {name}')
#     # /////////Вариант while
#     p = 0
#     while p < 5:
#         print(f'Привет {name}')
#         p += 1
# else:
#     print('Вы не ввели имя')

# Задание 2 ----------------------------------------------
# for i in range(101):
#     if i % 4 == 0: 
#         print(i)

# Задание 3 ----------------------------------------------
# faktorial = 1
# for i in range(2,11):
#     faktorial += i
# print(faktorial)

# Задание 4 ----------------------------------------------
# import random
# # Вариант 1
# # for i in range(4):
# #     rnd = random.randint(1, 1000)
# #     print(rnd)
# # Вариант 2
# gener = 1
# while gener < 5:
#     rnd = random.randint(1, 1000)
#     print(rnd)
#     gener += 1

# Задание 5 ----------------------------------------------
# text = 'караван'
# # print(text.count('а'))
# len = len(text)
# p = 0
# for i in range(len):
#     if text[i] == 'а':
#         p += 1
# print(p)

# Задание 6 ----------------------------------------------
# num1 = int(input('Введи начало диапазона: '))
# num2 = int(input('Введи конец диапазона: '))
# for i in range(num1,num2):
#     if (i % 3 == 0) and (i % 5 == 0):
#         print('Fizz Buzz')
#     elif i % 3 == 0: 
#         print('Fizz')
#     elif i % 5 == 0: 
#         print('Buzz')
#     else:
#         print(i)