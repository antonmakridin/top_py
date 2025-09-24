# number_1 = 4
# number_2 = 6

# def add(a, b):
#     res = a + b
#     return res

# res = add(number_1,number_2)
# print(res)

# users = []

# def add_user(name):
#     users.append(name)

# def show_users():
#     res = '\n'.join(users)
#     return res

# add_user('alisa')
# add_user('bob')
# add_user('vasya')
# print(show_users())



# #1
# def check_passwords(p1, p2):
#     if p1 == p2:
#         return True
#     else:
#         return False

# password1 = input("Введите первый пароль: ") # qwerty123
# password2 = input("Введите второй пароль: ") # qwerty123
# result = check_passwords(password1, password2) 
# print(result) # True

# #2
# def convert_currency(r, c):
#     currency = {
#     "USD": 79,
#     "EUR": 87,
#     "CNY": 12
#     }
#     value_currency = currency[c]
#     convert = r / value_currency
#     return convert
    
# rub_amount = float(input("Введите сумму в рублях: ")) # 1000 
# currency = input("Введите валюту (USD, EUR, CNY): ") # USD 
# converted = convert_currency(rub_amount, currency) 
# print(f"{rub_amount} рублей = {converted} {currency}") # 1000 рублей = 11.0 USD


# #3
# # Глобальный список 
# users = [] # Примеры вызова: 
# def add_user(name):
#     if name in users:
#         print('Пользователь существует')
#     else:
#         users.append(name)
#         print('Пользователь добавлен')
# add_user("Иван") 
# add_user("Анна") 
# add_user("Анна") 
# add_user("Петр")
# print(users) # ['Иван', 'Анна', 'Петр']


# #4
# users = []

# def add_user(name):
#     if name in users:
#         print('Пользователь существует')
#     else:
#         users.append(name)
#         print('Пользователь добавлен')

# def list_users():
#     res = ', '.join(users)
#     return res

# while True:
#     do = int(input('Выберите действие: \nДобавить пользователя - 1\nВывести всех пользователей - 2\nВыход - 3\n'))
#     if do == 1:
#         name = input('Введите имя пользователя: ')
#         add_user(name)
#     elif do == 2:
#         print(list_users())
#     elif do == 3:
#         print('До свидания!')
#         break

# #5
# import json

# def add_user():
#     name = input('Введите имя пользователя: ')
#     with open('2025-07-04\\users.json', 'r', encoding='utf-8') as f:
#         users = json.load(f)
#         for u in users:
#             if name == u['name']:
#                 print('Такой пользователь уже есть')
#                 break
#         else:
#             user = {
#                 "name": name
#             }
#             users.append(user)
#             with open('2025-07-04\\users.json', 'w', encoding='utf-8') as f:
#                 json.dump(users, f, ensure_ascii=True, indent=4)
#             print('Пользователь добавлен!\n')

# def list_users():
#     with open('2025-07-04\\users.json', 'r', encoding='utf-8') as f:
#         users = json.load(f)
#         print('\nПользователи:')
#         for u in users:
#             print(u['name'])

# while True:
#     do = int(input('Выберите действие: \nДобавить пользователя - 1\nВывести всех пользователей - 2\nВыход - 3\n'))
#     if do == 1:
#         add_user()
#     elif do == 2:
#         list_users()
#     elif do == 3:
#         print('До свидания!')
#         break


# #6
# import json

# def add_user():
#     name = input('Введите имя пользователя: ')
#     surname = input('Введите фамилию пользователя: ')
#     age = input('Введите возраст пользователя: ')
#     with open('2025-07-04\\users.json', 'r', encoding='utf-8') as f:
#         users = json.load(f)
#         for u in users:
#             if name == u['name']:
#                 print('Такой пользователь уже есть')
#                 break
#         else:
#             user = {
#                 "name": name,
#                 "surname": surname,
#                 "age": age
#             }
#             users.append(user)
#             with open('2025-07-04\\users.json', 'w', encoding='utf-8') as f:
#                 json.dump(users, f, ensure_ascii=True, indent=4)
#             print('Пользователь добавлен!\n')

# def list_users():
#     name = input('Введите имя пользователя: ')
#     with open('2025-07-04\\users.json', 'r', encoding='utf-8') as f:
#         users = json.load(f)
#         for u in users:
#             if name == u['name']:
#                 print('имя - ' + u['name']+'\n'+ 'фамилия - ' + u['surname'] + '\n' + 'возраст - ' + u['age'])
#                 break
#         else:
#             print('Такого пользователя не существует')

# while True:
#     do = int(input('Выберите действие: \nДобавить пользователя - 1\nВывести данные пользователя - 2\nВыход - 3\n'))
#     if do == 1:
#         add_user()
#     elif do == 2:
#         list_users()
#     elif do == 3:
#         print('До свидания!')
#         break



import json
import random
def take_word():
    with open('2025-07-04\\words.json', 'r', encoding='utf-8') as f:
        words = json.load(f)
        num = random.randint(1, len(words))
        for i in range(num - 1, num):
            word = words[i]
        value = word["word"]
        return value
        
def replace_word(word, word_user):
    ok = '_____'
    dict_upd = {}
    for j in range(5):
        if word[j] == word_user[j]:
            dict_upd.update({j: '*' + word_user[j] + '*'})
        elif word[j] != word_user[j] and word_user[j] in word:
            dict_upd.update({j: '-' + word_user[j] + '-'})
    new_ok = ' '.join(
        dict_upd.get(i, char)
        for i, char in enumerate(ok)
    )
    return new_ok

word = take_word()
print(word)
for i in range(1, 6):
    print(f'[Попытка {i}/5]. Введите слово: ')
    word_user = input()
    if len(word_user) != 5:
        print('Длина слова не 5 символов')
    else:
        if word == word_user:
            print('Угадал')
            break
        else:
            print(replace_word(word, word_user))
print('Не угадал')