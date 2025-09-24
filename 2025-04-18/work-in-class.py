# for i in range(3,5):
#     print('hello')
#     print(i)
# range (3,5,2) 3 - начальный, 5 - конечный, 2 - шаг итерации

# import random
# rnd = random.randint(1, 9)
# p = 0
# for i in range (9):
#     vvod = int(input('Введи число от 1 до 9: '))
#     p+=1
#     if vvod == rnd:
#         print('Угадал')
#         break
#     else:
#         print(f'Не угадал. Сыграем еще!')
# print(f'Количество попыток - {p}')

# import random
# rnd = random.randint(1, 9)
# vvod = int(input('Введи число от 1 до 9: '))
# # vvod = None   -  присвоение переменной ПУСТОТЫ или НИЧЕГО
# p = 1
# while vvod != rnd:
#     print('Не угадал. Сыграем еще!')
#     vvod = int(input('Введи число от 1 до 9: '))
#     p += 1
# print(f'Угадал! Количество попыток - {p}')



# ПРАКТИКА
# ЗАДАНИЕ 2
# ch1 = int(input('Введи начальное число цикла: '))
# ch2 = int(input('Введи конечное число цикла: '))
# for i in range(ch1,ch2+1):
#     print(i)

# ЗАДАНИЕ 2
# ch1 = int(input('Введи начальное число цикла: '))
# ch2 = int(input('Введи конечное число цикла: '))
# for i in range(ch1,ch2+1):
#     if i % 2 == 1: 
#         print(i)

# ЗАДАНИЕ 3
# text = input('Введи текст: ')
# len = len(text)
# for i in range(len):
#     print(text[i])

# ЗАДАНИЕ 4
# ch1 = int(input('Введи первое число: '))
# ch2 = int(input('Введи второе число: '))
# for i in range(ch1,ch2+1):
#     i += i
# print(i)
# sr = i / (ch2 - ch1)
# print(sr)

# ЗАДАНИЕ 5
# ch1 = int(input('Введи число: '))
# fakt = 1
# for i in range(2,ch1+1):
#     fakt *= i
# print(fakt)

# ЗАДАНИЕ 6
ch1 = int(input('Введи число повторений: '))
sym = input('Введи, что будем повторять: ')
# print(f'{sym*ch1}')
for i in range(ch1):
    print(sym, end='')