# #1
# with open('2025-06-24\\dz\\1.txt', 'r', encoding='utf-8') as file:
#     data = file.readlines()
#     for i in range(len(data)):
#         print(data[i].strip('\n'))


# #2
# with open('2025-06-24\\dz\\1.txt', 'r', encoding='utf-8') as file:
#     data = file.readlines()
#     for i in range(len(data)):
#         print(i, '-', data[i].strip('\n'))


# #3
# col = int(input('Сколько дел на завтра планируешь? '))
# with open('2025-06-24\\dz\\3.txt', 'w', encoding='utf-8') as file:
#     for _ in range(col):
#         name = input('Что нужно сделать?: ')
#         file.write(name + '\n')
#         print('Дело добавлено')
# print('Молодец, добавил 5 товаров\n')
# with open('2025-06-24\\dz\\3.txt', 'r', encoding='utf-8') as file:
#     data = file.readlines()
#     print('Завтра нужно сделать:')
#     for i in range(1, len(data) + 1):
#         print(i, '-', data[i-1].strip('\n'))


#4
while True:
    do = int(input('Выберите действие: \nДобавить сотрудника - 1\nПолучить должность сотрудника - 2\nВывести всех сотрудников - 3\nВыход - 4\n'))
    if do == 1:
        with open('2025-06-24\\dz\\4.txt', 'a', encoding='utf-8') as file:
            n = input('Укажи имя сотрудника: ')
            d = input('Укажи должность сотрудника: ')
            data = file.write('\n' + n + '-' + d)
            print('Сотрудник добавлен! \n')
    elif do == 2:
        with open('2025-06-24\\dz\\4.txt', 'r', encoding='utf-8') as file:
            n = input('Введи имя сотрудника: ')
            data = file.readlines()
            for i in range(len(data)):
                dat = data[i].strip()
                dat = dat.split('-')
                if dat[0] == n:
                    print('Должность сотрудника', dat[0], '-', dat[1], '\n')
                    break
            else:
                print('Такого сотрудника нет \n')
    elif do == 3:
        with open('2025-06-24\\dz\\4.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
            print('Имя / Должность')
            for i in range(len(data)):
                dat = data[i].strip()
                dat = dat.split('-')
                print(dat[0], '/', dat[1])
    elif do == 4:
        break