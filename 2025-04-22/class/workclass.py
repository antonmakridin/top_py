# 1
# chislo = int(input('Введите число: '))
# if chislo:
#     for i in range(1,10):
#         print(f'{chislo} * {i} = {chislo*i}')
# else:
#     print('не ввели число')
# for i in range(1,10):
#     for j in range(1,10):
#         print(f'{i} * {j} = {i*j}')

# 2
# p = 1
# while p < 11:
#     print(f'{p}')
#     p += 1

# 3
# import time, os
# chislo = int(input('Введите число: '))
# os.system('cls||clear')
# while chislo >= 1:
#     print(f'{chislo}')
#     chislo -= 1
#     time.sleep(1)
#     os.system('cls||clear')
# print('Время истекло')

# 4
# itogo = 0
# while True:
#     chislo = int(input('Введите число: '))
#     if chislo != 0:
#         itogo += chislo
#     else:
#         print(itogo)
#         break

# 5
# import random
# rnd = random.randint(1, 9)
# vvod = int(input('Введи число от 1 до 9: '))
# p = 1
# while True:
#     print('Не угадал. Сыграем еще!')
#     vvod = int(input('Введи число от 1 до 9: '))
#     p += 1
#     if vvod == rnd:
#         print(f'Угадал! Количество попыток - {p}')
#         break

# 6
print('Обменник')
while True:
    ch1 = int(input('Введи количество денег для перевода: '))
    do = int(input('Выбери действие: \n 1. Перевести в доллары \n 2. Перевести в евро \n 3. Перевести в юани \n 4. Выход \n'))
    if do == 1:
        print(f'Вы получите {ch1/81.6} долларов')
    elif do == 2:
        print(f'Вы получите {ch1/93.44} евро')
    elif do == 3:
        print(f'Вы получите {ch1/11.19} юаней')
    elif do == 4:
        print('До свидания! Приходите еще в наш обменник.')
        break

# 7
# text = input('Введи текст: ')
# len = len(text)
# ch = 0
# b = 0
# for i in range(len):
#     if text[i].isdigit() == True:
#         ch += 1
#     if text[i].isalpha() == True:
#         b += 1
# print(f'Цифр в строке - {ch}')
# print(f'Символов в строке - {b}')

# 8
# chislo = input('Введи число: ')
# len = len(chislo)
# itogo = 0
# for i in range(len):
#     if chislo[i].isdigit():
#         itogo += int(chislo[i])
# print(f'Цифр в строке - {itogo}')
