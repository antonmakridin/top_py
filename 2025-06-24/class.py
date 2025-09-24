# file = open('2025-06-24\\data.txt', encoding='utf-8')

# data = file.read()
# print(data)

# file.close()

# file = open('2025-06-24\\data.txt', encoding='utf-8')
# data = file.readlines()
# for i in range(len(data)):
#     print(f'{i + 1}. {data[i].strip('\n')}')
# file.close()



#создание и запись в файл
# file = open('2025-06-24\\data1.txt', 'a', encoding='utf-8')
# file.write('привет\n')
# file.write('пока\n')
# file.close()


# запись списка в файл
# file = open('2025-06-24\\data1.txt', 'a', encoding='utf-8')
# city = ['Екб\n', 'Москва\n']
# file.writelines(city)
# file.close()



# with open('2025-06-24\\data2.txt', 'a', encoding='utf-8') as file:
#     city = ['Екб\n', 'Москва\n']
#     file.writelines(city)

# print('сохранено')


# #запись списка в файл
# with open('2025-06-24\\data3.txt', 'a', encoding='utf-8') as file:
#     names = ['Alisa', 'Bob', 'John']
#     for name in names:
#         file.write(name)
#         file.write('\n')

# print('сохранено')

# #запись в файл информации от пользователя
# name = input('Введи имя: ')
# print('Добавляю в файл...')
# with open('2025-06-24\\users.txt', 'w', encoding='utf-8') as file:
#     file.write(name)
# print(f'Имя {name} добавлено в файл')



#1
# with open('2025-06-24\\1.txt', 'r', encoding='utf-8') as file:
#     data = file.readlines()
#     for i in range(len(data)):
#         print(data[i].strip('\n'))



# #2
# with open('2025-06-24\\1.txt', 'r', encoding='utf-8') as file:
#     data = file.readlines()
#     for i in range(len(data)):
#         print(f'{i} - {data[i].strip('\n')}')


# #3
# with open('2025-06-24\\3.txt', 'a', encoding='utf-8') as file:
#     for _ in range(5):
#         name = input('Укажи название товара: ')
#         file.write(name)
#         file.write('\n')
#         print('Товар добавлен')
# print('Молодец, добавил 5 товаров')

# #4
# with open('2025-06-24\\4.txt', 'r', encoding='utf-8') as file:
#     l = input('Введи логин: ')
#     p = input('Введи пароль: ')
#     data = file.readlines()
#     for i in range(len(data)):
#         dat = data[i].strip('\n')
#         dat = dat.split('-')
#         if dat[0] == l and dat[1] == p:
#             print('Доступ разрешен')
#             break
#     else:
#         print('Доступ запрещен')

#5
do = int(input('Выберите действие: \nАвторизация - 1\nРегистрация - 2\nВыход - 3\n'))
if do == 1:
    with open('2025-06-24\\5.txt', 'r', encoding='utf-8') as file:
        l = input('Введи логин: ')
        p = input('Введи пароль: ')
        data = file.readlines()
        for i in range(len(data)):
            dat = data[i].strip('\n')
            dat = dat.split('-')
            if dat[0] == l and dat[1] == p:
                print('Доступ разрешен')
                break
        else:
            print('Доступ запрещен')
elif do == 2:
    with open('2025-06-24\\5.txt', 'a', encoding='utf-8') as file:
        l = input('Введи логин: ')
        p = input('Введи пароль: ')
        p2 = input('Введи пароль еще раз: ')
        if p == p2:
            data = file.write('\n' + l + '-' + p)
            print('Успешная регистрация')
        else:
            print('Пароли не совпадают. Регистрация не пройдена')
elif do == 3:
    exit