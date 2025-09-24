# #1
# numbers = [12, 34, 2 ,3, 46]
# for i in range(5):
#     print(numbers[i])
# for num in numbers:
#     print(num)


#2
# dela = []
# for i in range(3):
#     d = input('Введите дело ')
#     dela.append(d)
# print(dela)

# #3
# users = ['Алиса', 'Боб', 'Чарли']
# n = input()
# if n in users:
#     print('Доступ разрешен')
# #или
# # for name in users:
# #     if n == name:
# #         print('Доступ разрешен')
# #или
# if users.index(n):
#     print('Доступ разрешен')
# #ошибка в случае отсутствия вводимого значения в списке

# #4
# string = 'в это предложении пять слов'
# print(len(string.split()))

# #5
# import random
# pril = ['красивый', 'мудрый', 'волнующий', 'печальный']
# su = ['закат', 'ключ', 'эксперимент', 'код']
# rp = ['единорога', 'ребенка', 'президента', 'вселенной']
# for i in range(3):
#     print(random.choice(pril) + ' ' + random.choice(su) + ' ' + random.choice(rp))


#6
# numbers = [[1, 2, -4], [6, -1, 3], [-12, 7, 8], [12, -4, 5]]
# res = []
# for num in numbers:
#     sum = 0
#     for i in range(3):
#         if num[i] > 0:
#             sum += num[i]
#     res.append(sum)
# print(res)

#7
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

# #8
# question = [['Столица Италии', 'Рим'], ['Длинная река в Египте', 'Нил'], ['Самый большой океан', 'Тихий']]
# for q in question:
#     otvet = True
#     o = input(q[0] + ' ')
#     if o != q[1]:
#         otvet = False
#         print('Неправильный ответ')
#     else:
#         print('Правильный ответ')

#9
numbers = [12, 34, 2, 3, 46, 1]
sort = []
while numbers:
    min1 = numbers[0]
    for num in numbers:
        if num < min1:
            min1 = num
    sort.append(min1)
    numbers.remove(min1)
print(sort)


# numbers = [12, 34, 2, 3, 46]
# sort = []
# for i in range(len(numbers)):
#     min1 = min(numbers)
#     sort.append(min1)
#     numbers.remove(min1)
# print(sort)