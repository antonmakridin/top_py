#поиск буквы в заданном слове
# word = 'черезстрочно'
# letter = input('Введи букву: ')
# if word.count(letter):
#     print('молодец')
# else:
#     print('не молодец')

# вывод количества символов
# string = input('Введи текст: ')
# print(f'Количество символов = {len(string)}')

#подсчет количества вхождений буквы в строке
# word = input('Введи слово: ')
# print(f'Количество букв о с учетом регистра - {word.count('о')}')
# word = word.lower()
# print(f'Количество букв о без учета регистра - {word.count('о')}')

#ввод логина и пароля
# login = input('Логин: ')
# passwd = input('Пароль: ')
# log_admin = 'admin'
# log_passwd = 'PwD'
# if login.lower() == log_admin and passwd == log_passwd:
#     print('доступ разрешен')
# else:
#     print('доступ запрещен')

#проверка содержимого строки
# string = input('Введи какие-то данные: ')
# if len(string) == 0:
#     print('Вы не указали данные')
#     exit
# else:
#     string.isdigit() #Проверяет, состоит ли строка только из цифр.
#     string.isalpha() #Проверяет, состоит ли строка только из букв.
#     string.isalnum() #Проверяет, состоит ли строка только из букв и цифр.
#     if string.isdigit() and not string.isalpha():
#         print('Строка состоит только из цифр')
#     elif string.isalpha() and not string.isdigit():
#         print('Строка состоит только из букв')
#     else:
#         print('Строка состоит из разных символов')

#проверка на палиндром
# string = input('Введите палиндром (или нет ))): ')
# if len(string) == 0:
#     print('Вы не указали данные')
#     exit
# else:
#     string = string.replace(' ','')
#     string = string.lower()
#     if string == string[::-1]:
#         print('Вы ввели палиндром')
#     else:
#         print('Вы ввели белеберду')

import random
i = 0
while i<5:
    variant = input('Введите ваш выбор: ')
    variant = variant.lower()

    rnd = random.randint(1, 3)
    if variant == 'камень':
        variant = 1
    elif variant == 'ножницы':
        variant = 2
    elif variant == 'бумага':
        variant = 3
    if (variant == 1 and rnd == 2) or (variant == 2 and rnd == 3) or (variant == 3 and rnd == 1):
        print('Выиграл')
        break
    elif variant == rnd:
        print('Ничья')
    else:
        if rnd == 1:
            rndv = 'Камень'
        elif rnd == 2:
            rndv = 'Ножницы'
        elif rnd == 3:
            rndv = 'Бумага'
        print(f'У меня {rndv}. Ты проиграл. Сыграем еще')
    i+=1