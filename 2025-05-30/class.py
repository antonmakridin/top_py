# #9
# from random import randint
# i = 1
# s = randint(1, 10)
# while i < 4:
#     n = int(input('Введи число от 1 до 10: '))
#     if n == s:
#         print(f'Угадал с {i} попытки')
#         break
#     i += 1
# if i == 4:
#     print(f'не угадал, было число {s}')


#10
# for i in range(25, 61):
#     if i % 5 == 0:
#         print(i, 'кратно 5')
#     elif i % 3 == 0:
#         print(i, 'кратно 3')
#     elif i == 42:
#         print('Это секретное число')
#     else:
#         print(i)


#11
# passw = 'a2c9a'
# for _ in range(5):
#     pos = 0
#     mesto = 0
#     yes_in = []
#     not_in = []
#     p = input('Введи пароль: ')
#     for i in range(5):
#         if p[i] == passw[i]:
#             pos += 1
#             yes_in.append(p[i])
#         else:
#             not_in.append(p[i])
#     for j in range(len(not_in)):
#             if not_in[j] in passw:
#                 mesto +=1
#     print(f'совпало по позиции: {pos}')
#     print(f'не на своем месте: {mesto}')


# # #12
# n = int(input('Укажи количество чисел в массиве: '))
# mas = []
# for i in range(1, n + 1):
#     s = int(input(f'Введи {i} из {n} число: '))
#     mas.append(s)
# max1 = mas[0]
# min1 = mas[0]
# for num in mas:
#     if num > max1:
#         max1 = num
#     if num < min1:
#         min1 = num
# print(f'Максимальная разница значений {min1} и {max1} составляет {abs(abs(min1) - abs(max1))}')



# words1 = ['собака', 'кошка']
# words2 = ['dog', 'cat']
# user  = input('Введи слово: ')
# print(words2[words1.index(user)])


words = {'собака': 'dog', 'кот': 'cat'}
# добавить в словарь
words['стол'] = 'table'
user  = input('Введи слово: ')
print(words[user])