# задание 1 проверка пароля
# passwd = input('Введите пароль: ')
# must = '$'
# min_sym = 8
# вариант 1
# if len(passwd) >= min_sym and must in passwd:
#     print('Пароль подходит')
# else:
#     print('Пароль не подходит')
# вариант 2
# if len(passwd) >= 8 and passwd.find(must) > 1:
#     print('Пароль подходит')
# else:
#     print('Пароль не подходит')


# задание 2 вывод символов
# string = input('Введи какие-то данные: ')
# if len(string) > 0:
#     first_sym = string[0]
#     last_sym = string[-1]
#     print(f'Первый символ: "{first_sym}", последний символ "{last_sym}"')
# else:
#     print("Строка пустая.")


# задание 3 индекс входждения символа
text = input("Введите какие-то данные: ")
sym = input("Введите символ: ")
# if len(sym) != 1:
#     print("Пожалуйста, введите только один символ.")
# else:
# вариант 1
#     if sym in text:
#         index = text.index(sym)
#         print(f"Символ найден. Индекс первого вхождения: {index}")
#     else:
#         print("Символ отсутствует.")
# вариант 2
    # if text.find(sym) > 1:
    #     index = text.index(sym)
    #     print(f"Символ найден. Индекс первого вхождения: {index}")
    # else:
    #     print("Символ отсутствует.")


# задание 4 замена пробелов
#text = input("Введите какие-то данные: ")
#print(f'Измененный текст {text.replace(" ", "1")}')