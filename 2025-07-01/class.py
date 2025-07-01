# def square(a, b):
#     res = a * b
#     return res

# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i, '+', j, '=', square(i, j))

# сумма чисел в списке
# s = [5, 7, 3]

# def summa(spisok):
#     summa = 0
#     for t in spisok:
#         summa += t
#     return summa

# print(summa(s))
# print(sum(s))



#3
# def distance(s, t):
#     dist = s * t
#     return dist
# s = int(input('Введите скорость: '))
# t = int(input('Введите время: '))
# print(distance(s, t))


# #4
# def fakt(a):
#     faktorial = 1
#     if a > 0:
#         for i in range(1, a + 1):
#             faktorial *= i
#     print(faktorial)
# n = int(input('Введите число: '))
# fakt(n)


# #6
def summa(a, b):
    print(a + b)
def raznost(a, b):
    print(a - b)
def square(a, b):
    print(a * b)
def division(a, b):
    if b != 0:
        print(a / b)
    else:
        print('На ноль делить нельзя!')
while True:
    do = input('Что сделать надо? 1 - сложить, 2 - вычесть, 3 - перемножить, 4 - разделить, 0 - Выход: ')
    if do == "0":
        break
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    if do == "1":
        summa(a, b)
    elif do == "2":
        raznost(a, b)
    elif do == "3":
        square(a, b)
    elif do == "4":
        division(a, b)
    else:
        print('Ошибка')

# #7
# def clear(s):
#     new_s = []
#     for n in s:
#         if n.isalpha():
#             new_s.append(n)
#     return ''.join(new_s)
# s = 'привет2312??как77712дела22312'
# print(clear(s))


# #8
# def fib(n):
#     fi = [0, 1]
#     for _ in range(2, n):
#         fi.append(fi[-2] + fi[-1])
#     print(fi)
# n = int(input('Укажите количество чисел ряда Фибоначчи: '))
# if n == 0:
#     print('Такого числа нет')
# elif n == 1:
#     print('[0]')
# else:
#     fib(n)


    