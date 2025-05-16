# name = 'koko'
# print(f'привет {name}')
# print('vasya')


# print(13 // 12)
# print(9 // 12)
# print(9 % 12)
# print(84 // 12)
# print(82 // 3**2 % 7)
# print((1 - 1) // 4 + 1)

# n = int(input())
# digit3 = n // 10000
# digit = n % 10000 // 1000
# digit2 = n % 1000 // 100
# digit1 = n % 100 // 10
# digit0 = n % 10
# printff = "22"
# _s = printff
# print(_s)

# n = int(input())
# n2 = n % 10 + n * 10
# n3 = n2 + n * 100
# print(n + n2 + n3)

# a = int(input())
# a1 = a // 1000
# a2 = a % 1000 // 100
# a3 = a % 100 // 10
# a4 = a % 10
# print(a1, a2, a3, a4)

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a < b and a < c and a < d:
#     print(a)
# if b < a and b < c and b < d:
#     print(b)
# if c < a and c < b and c < d:
#     print(c)
# if d < a and d < b and d < c:
#     print(d)

# age = int(input())
# if age <= 13:
#     print('детство')
# if 14 <= age <= 24:
#     print('молодость')
# if 25 <= age <= 59:
#     print('зрелость')
# if age >= 60:
#     print('старость')


# num1 = 34
# num2 = 81
# if num1 // 9 == 0 or num2 % 9 == 0:
#     print('число', num1, 'выиграло')
# else:
#     print('число', num1 // 9, 'выиграло')

# x = int(input())
# if x % 7 == 0 or x % 17 == 0:
#     print('YES')
# else:
#     print(x % 7, x % 17)


# a, b, c = int(input()), int(input()), int(input())
# if a + b > c and a + c > b and b + c > a:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a - 1 <= c <= a + 1 and b - 1 <= d <= b + 1:
#     print('YES')
# else:
#     print('NO')


# a = input()
# b = input()
# if not (a == 'красный' or a == 'синий' or a == 'желтый') or not (b == 'красный' or b == 'синий' or b == 'желтый'):
#     print('ошибка цвета')
# else:
#     if (a == 'красный' and b == 'синий') or (b == 'красный' and a == 'синий'):
#         print('фиолетовый')
#     elif (a == 'красный' and b == 'желтый') or (b == 'красный' and a == 'желтый'):
#         print('оранжевый')
#     elif (a == 'синий' and b == 'желтый') or (b == 'синий' and a == 'желтый'):
#         print('зеленый')
#     elif a == b:
#         print(a)
#     else:
#         print('ошибка цвета')

# a = int(input())
# g = 'зеленый'
# r = 'красный'
# b = 'черный'
# if a < 0 or a > 36:
#     print('ошибка ввода')
# elif a == 0:
#     print(g)
# else:
#     if (0 < a <= 10 or 18 < a <= 28) and (a % 2 == 0):
#         print(b)
#     elif (0 < a <= 10 or 18 < a <= 28) and (a % 2 != 0):
#         print(r)
#     if (10 < a <= 18 or 28 < a <= 36) and (a % 2 == 0):
#         print(r)
#     elif (10 < a <= 18 or 28 < a <= 36) and (a % 2 != 0):
#         print(b)
    
# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
# if b1 < a2 or b2 < a1:
#     print('пустое множество')
# elif b1 == a2:
#     print(a2)
# elif a1 == b2:
#     print(a1)
# elif a1 <= a2 and b1 < b2 and a2 < b1:
#     print(a2, b1)
# elif a1 <= a2 and b2 <= b1:
#     print(a2, b2)
# elif a2 <= a1 and b1 <= b2:
#     print(a1, b1)
# elif a2 <= a1 and b2 <= b1:
#     print(a1, b2)
# else:
#     print('пустое множество')

# y = int(input())
# if y // 100 == 0:
#     print('YES')
# else:
#     print(y % 100)

# a = int(input())
# if a == 1:
#     print('I')
# elif a == 2:
#     print('II')
# elif a == 3:
#     print('III')
# elif a == 4:
#     print('IV')
# elif a == 5:
#     print('V')
# elif a == 6:
#     print('VI')
# elif a == 7:
#     print('VII')
# elif a == 8:
#     print('VIII')
# elif a == 9:
#     print('IX')
# elif a == 10:
#     print('X')
# else:
#     print('ошибка')

# a = int(input())
# if a % 2 != 0:
#     print('YES')
# elif 2 <= a <= 5 and a % 2 == 0:
#     print('NO')
# elif 6 <= a <= 20 and a % 2 == 0:
#     print('YES')
# elif a > 20 and a % 2 == 0:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a - c == b - d or a - c == d - b:
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (c - a == 1 or c - a == -1) and (d - b == 2 or d - b == -2):
#     print('YES')
# elif (c - a == 2 or c - a == -2) and (d - b == 1 or d - b == -1):
#     print('YES')
# else:
#     print('NO')



# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if a - c == b - d or a - c == d - b or a == c or b == d:
#     print('YES')
# else:
#     print('NO')

# y = int(input())
# p = 0
# if 0 < y <= 2:
#     p += y * 10.5
# elif y > 2:
#     p += (y - 2) * 4 + 10.5 * 2
# print(p)

# x = float(input())
# y = int(x)
# z = int((x - y) * 10)
# print(z)

# a, b, c = int(input()), int(input()), int(input())
# ma = max(a, b, c)
# mi = min(a, b, c)
# sr = a + b + c - ma - mi
# print(ma, mi, sr, end = '/n')

# n = int(input())
# a = n % 1000 // 100
# b = n % 100 // 10
# c = n % 10
# ma = max(a, b, c)
# mi = min(a, b, c)
# sr = ma - mi
# ser = a + b + c - ma - mi
# if sr == ser:
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# s = 'https://pygen.ru/'
# if 'a' in s:
#     print('Введенная строка содержит символ а')
# else:
#     print('Введенная строка не содержит символ а')

# s = 'Sigma'
# print('a' in s)
# print('z' in s)

# print('ab' in 'abc')
# print('ac' in 'abc')
# s = input()
# if 'суббота' or 'воскресенье' in s:
#     print('YES')
# else:
#     print('NO')

# import math
# num1 = math.sqrt(2)     # вычисление квадратного корня из двух
# num2 = math.ceil(3.8)   # округление числа вверх
# num3 = math.floor(3.8)  # округление числа вниз
# print(num1)
# print(num2)
# print(num3)



# from math import sqrt, ceil
# print(sqrt(25))
# print(ceil(34.7))
# print(floor(12.8))  # приведет к ошибке, так как функция floor не подключена



# import math
# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
# print(math.sqrt(pow((x1-x2), 2)+pow((y1-y2), 2)))

# import math
# R = float(input())
# print(math.pi*R**2)
# print(2*math.pi*R)

# import math
# a, b = float(input()), float(input())
# print((a + b) / 2)
# print(math.sqrt(a * b))
# print((2 * a * b) / (a + b))
# print(math.sqrt((a**2 + b**2) / 2))

# import math
# x = float(input())
# x = x * math.pi / 180
# print(math.sin(x) + math.cos(x) + (math.tan(x))**2)

# import math
# x = float(input())
# print(math.floor(x) + math.ceil(x))

# import math
# a, b, c = float(input()), float(input()), float(input())
# D = pow(b, 2) - 4 * a * c
# if D == 0:
#     print(-b / (2 * a))
# elif D > 0:
#     x1 = ((-b - math.sqrt(D)) / (2 * a))
#     x2 = ((-b + math.sqrt(D)) / (2 * a))
#     if x1 < x2:
#         print(x1)
#         print(x2)
#     else:
#         print (x2)
#         print (x1)
# elif D < 0:
#     print('Нет корней')

# import math
# n, a = int(input()), float(input())
# print((n * pow(a, 2)) / (4 * math.tan(math.pi / n)))

# for i in range(5):
#     num = int(input())
#     print("Квадрат вашего числа равен:", num * num)
# print("Цикл завершен")


# s = int(input())
# for i in range(s, 0, -1):
#     print('*' * i)

m, p, n = int(input()), int(input()), int(input())
print('1', float(m))
for i in range(n-1):
    m = m + m * p / 100
    print(i + 2, m)