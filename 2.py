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

# m, p, n = int(input()), int(input()), int(input())
# print('1', float(m))
# for i in range(n-1):
#     m = m + m * p / 100
#     print(i + 2, m)

# count = 0
# while count < 5:
#     print("Счетчик:", count)
#     count += 1


# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     if i % 17 == 0:
#         print(i)
#     elif i % 10 == 9:
#         print(i)
#     elif (i % 3 == 0) and (i % 5 == 0):
#         print (i)

# x = int(input())
# for i in range(10):
#     print(x, 'x', i + 1, '=', x * (i + 1))

# counter1 = 0
# counter2 = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter1 = counter1 + 1
#     if num == 0:
#         counter2 = counter2 + 1
# print('Было введено', counter1, 'чисел, больших 10.')
# print('Было введено', counter2, 'нулей.' )



# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1

# print(counter)


# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')

# n = int(input())
# ch = 0
# for i in range(n):
#     v = int(input())
#     ch += v
# print(ch)

# from math import log
# m = 0
# n = int(input())
# for i in range(n):
#     m += (1 / (i + 1))
# print(m - log(n))


# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     if i**2 % 10 == 2 or i**2 % 10 == 5 or i**2 % 10 == 8:
#         sum += i
# print(sum)

# from math import factorial
# n = int(input())
# print(factorial(n))

# sum = 1
# for i in range(10):
#     n = int(input())
#     if n != 0:
#         sum *= n
# print(sum)

# sum = 0
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         sum += i
# print(sum)

# from math import pow
# sum = 0
# n = int(input())
# for i in range(1, n + 1):
#     sum += pow((-1), i + 1) * i
# print(int(sum))

# n = int(input())
# numbers = [int(input()) for _ in range(n)]
# max1 = max(numbers)
# numbers.remove(max1)
# max2 = max(numbers)
# print(max1)
# print(max2)

# ch = 0
# for i in range(10):
#     num = int(input())
#     if num % 2 != 0:
#         ch += 1
# if ch > 0:
#     print('NO') 
# else:
#     print('YES')


# fib = [1, 1, 3, 4]
# e = []
# for i in range(n):
#     fib.append[n]
# print(fib)

# n = int(input())
# if n == 0:
#     print('')
# elif n == 1:
#     print('1')
# else:
#     fib = [1,1]
#     for i in range(2, n):
#         fib.append(fib[i-1]+ fib[i-2])
#     print(' '.join(map(str, fib)))

# numbers = [12, 4, 5, -3, 12, -6, 1, 7, 2]
# for i in range(len(numbers)):
#     if numbers[i] < 0:
#         otr += numbers[i]


# i = 5
# while i <= 12:
#     print('Python awesome!')
#     i += 1

# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)

# i = input()
# total = ""
# flag = True
# while flag == True:
#     total += i+"\n"
#     i = input()
#     if i == "КОНЕЦ" or i == "конец":
#         flag = False
# print(total)


# total = 0
# flag = True
# while flag == True:
#     i = input()
#     if i == "стоп" or i == "хватит" or i == "достаточно":
#         flag = False
#     else:
#         total += 1
# print(total)

# i = int(input())
# total = 0
# while i >= 0:
#     total += i
#     i = int(input())
# print(total)

# total = 0
# flag = True
# while flag == True:
#     i = int(input())
#     if i <= 0 or i > 5:
#         flag = False
#     else:
#         if i == 5:
#             total += 1
# print(total)

# total1 = 0
# total2 = 0
# total3 = 0
# total4 = 0
# ost25 = 0
# flag = True
# s = int(input())
# y = s
# m = [25, 10, 5, 1]
# while flag == True:
#     s -= m[0]
#     if s >= 0:
#         total1 += 1
#     else:
#         ost25 = y - total1 * m[0]
#         flag = False
# if ost25 == 0:
#     print(total1)
# else:
#     flag = True
#     ost10 = 0
#     y = ost25
#     while flag == True:
#         ost25 -= m[1]
#         if ost25 >= 0:
#             total2 += 1
#         else:
#             ost10 = y - total2 * m[1]
#             flag = False
#     if ost10 == 0:
#         print(total1 + total2)
#     else:
#         flag = True
#         ost5 = 0
#         y = ost10
#         while flag == True:
#             ost10 -= m[2]
#             if ost10 >= 0:
#                 total3 += 1
#             else:
#                 ost5 = y - total3 * m[2]
#                 flag = False
#         if ost5 == 0:
#             print(total1 + total2 + total3)
#         else:
#             flag = True
#             ost1 = 0
#             y = ost5
#             while flag == True:
#                 ost5 -= m[3]
#                 if ost5 >= 0:
#                     total4 += 1
#                 else:
#                     flag = False
#             if ost1 == 0:
#                 print(total1 + total2 + total3 + total4)

# n = int(input())
# coins = [25, 10, 5, 1]
# count = 0
# for coin in coins:
#     if n >= coin:
#         num = n // coin
#         count += num
#         n -= num * coin
#     if n == 0:
#         break
# print(count)

# #Напишем программу, которая считывает натуральное число (целое положительное) и обрабатывает его цифры.
# n = int(input())
# while n != 0:  # пока в числе есть цифры
#     last_digit = n % 10  # получить последнюю цифру
#     # код обработки последней цифры
#     n = n // 10  # удалить последнюю цифру из числа


# #Напишем программу, которая определяет, есть ли в числе цифра 7.
# num = int(input())
# has_seven = False  # сигнальная метка
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
# if has_seven == True:
#     print('YES')
# else:
#     print('NO')

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

# n = int(input())
# x = []
# while n != 0:
#     last = n % 10
#     x.append(last)
#     n = n // 10
# print(''.join(map(str, x)))

# n = int(input())
# while n != 0:
#     last = n % 10
#     print(last, end='')
#     n = n // 10


# n = int(input())
# m = n
# min = n % 10
# max = n % 10
# while n != 0:
#     last = n % 10
#     n = n // 10
#     if last < min:
#         min = last
#     if last > max:
#         max = last
# print('Максимальная цифра равна', max)
# print('Минимальная цифра равна', min)



# n = int(input())
# sc = 0
# col = 0
# pr = 1
# first = n
# posl = n % 10
# srar = 0
# sumpp = 0
# while n != 0:
#     last = n % 10
#     sc += last
#     col += 1
#     pr *= last
#     n = n // 10
# first = first // (10**(col-1))
# print(sc)
# print(col)
# print(pr)
# print(sc / col)
# print(first)
# print(first + posl)

# n = int(input())
# col = 0
# first = n
# while n != 0:
#     last = n % 10
#     col += 1
#     n = n // 10
# first = first // (10**(col-2))
# second = first % 10
# print(second)


# n = int(input())
# l = n % 10
# da = 0
# while n != 0:
#     last = n % 10
#     if last != m:
#         da += 1
#     n = n // 10
# if da == 0:
#     print('YES')
# else:
#     print('NO')


# n = int(input())
# l = n % 10
# pl = (n // 10) % 10
# razn = l - pl
# da = 0
# while n != 0:
#     last = n % 10
#     n = n // 10
#     pr = n % 10
#     if last - pr != razn:
#         da += 1
# if da == 0:
#     print('YES')
# else:
#     print('NO')


# n = int(input())
# l = n % 10
# da = 0
# while n != 0:
#     last = n % 10
#     n = n // 10
#     pr = n % 10
#     if last > pr and pr != 0:
#         da += 1
# if da == 0:
#     print('YES')
# else:
#     print('NO')


# n = int(input())
# for i in range(2, n+1):
#     if n % i == 0:
#         break
# print(i)


# n = int(input())
# for i in range(1, n+1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)
#     57.255822, 65.301458


# s = 0
# mx = - 10 ** 6
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#     if mx < x < 0:
#         mx = x
# if s != 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')



# n = int(input())
# max_digit = -1
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n = n // 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)



# n = int(input())
# z = n
# t = 1
# while n >= 10:
#     n //= 10
#     t += 1
# for i in range(t - 3):
#     z //= 10
# z = z % 10
# print(z)

# n = int(input())
# product = 1
# while n > 1:
#     digit = n % 10
#     product *= digit
#     n //= 10
#     print(digit, product, n)
# print(product)


# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10

# print(counter)

# n = int(input())
# for i in range(n):
#     for j in range(5):
#         print(i + 1, end=' ')
#     print()


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(i):
#         print(i, end='')
#     print()

# import time
# def find_solution(max_limit):
#     # Создаем словарь для хранения пятых степеней чисел
#     fifth_powers = {x: x**5 for x in range(1, max_limit + 1)}
#         # Проходим все возможные комбинации a, b, c, d (a <= b <= c <= d)
#     for a in range(1, max_limit + 1):
#         for b in range(a, max_limit + 1):
#             for c in range(b, max_limit + 1):
#                 for d in range(c, max_limit + 1):
#                     sum_fifth = fifth_powers[a] + fifth_powers[b] + fifth_powers[c] + fifth_powers[d]
#                     # Проверяем, является ли сумма пятых степеней пятой степенью какого-либо числа
#                     e = round(sum_fifth ** (1/5))
#                     # Учитываем погрешность округления
#                     if e**5 == sum_fifth and e <= max_limit:
#                         print(f"Найдено решение: {a}⁵ + {b}⁵ + {c}⁵ + {d}⁵ = {e}⁵")
#                         print(f"Проверка: {a**5} + {b**5} + {c**5} + {d**5} = {e**5}")
#                         print(f"Проверка2: {a + b + c + d + e}")
#                         return (a, b, c, d, e)
#     print("Решение не найдено в заданном диапазоне.")
#     return None
# # Задаем максимальное значение для перебора (можно увеличить для поиска большего количества решений)
# max_limit = 150
# start_time = time.time()
# solution = find_solution(max_limit)
# end_time = time.time()
# print(f"Время выполнения: {end_time - start_time:.2f} секунд")


# n = int(input())
# c = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(c, end=' ')
#         c += 1
#     print()


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for j in range(i - 1, 0, -1):
#         print(j, end='')
#     print()



# b = int(input())
# for num in range(1, b + 1):
#     col = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             col += 1
#     print(num, end='')
#     for c in range(col):
#         print('+', end='')
#     print()


# n = int(input())
# t = 0
# s = 0
# while n > 0:
#     t = n % 10
#     n //= 10
#     s += t
# while s > 0:


# n = int(input())
# i = 2
# while n % i != 0:
#     i += 1
# <<<<<<< HEAD
# print(i)



# n = int(input())
# digits = [int(d) for d in str(n)]  # Преобразуем число в список цифр

# # 1. Количество цифр 3
# count_3 = digits.count(3)

# # 2. Сколько раз встречается последняя цифра
# last_digit = digits[-1]
# count_last = digits.count(last_digit)

# # 3. Количество чётных цифр
# count_even = sum(1 for d in digits if d % 2 == 0)

# # 4. Сумма цифр, больших пяти
# sum_gt5 = sum(d for d in digits if d > 5)

# # 5. Произведение цифр, больших семи
# product_gt7 = 1
# for d in digits:
#     if d > 7:
#         product_gt7 *= d

# # 6. Сколько раз встречаются цифры 0 и 5 (суммарно)
# count_0_5 = digits.count(0) + digits.count(5)

# # Выводим результаты
# print(count_3)
# print(count_last)
# print(count_even)
# print(sum_gt5)
# print(product_gt7)
# print(count_0_5)


# # Словарь для хранения чисел и их представлений в виде суммы кубов
# from collections import defaultdict

# sums = defaultdict(list)
# max_num = 25000  # Достаточно большое число, чтобы найти первые 5 чисел

# # Перебираем все возможные пары (a, b), где a <= b, чтобы избежать повторов
# for a in range(1, int(max_num ** (1/3)) + 2):
#     for b in range(a, int(max_num ** (1/3)) + 2):
#         cube_sum = a**3 + b**3
#         if cube_sum <= max_num:
#             sums[cube_sum].append((a, b))

# # Находим числа, у которых есть хотя бы два разных представления
# ramanujan_numbers = []
# for num in sums:
#     if len(sums[num]) >= 2:
#         ramanujan_numbers.append(num)

# # Сортируем и выводим первые 5 чисел (включая 1729)
# ramanujan_numbers_sorted = sorted(ramanujan_numbers)
# print("Первые 5 чисел, выражаемых как сумма двух кубов двумя разными способами:")
# for num in ramanujan_numbers_sorted[:5]:
#     print(num)
# # print(i)


# string = "abcd1234abcd1234"
# for i in range(len(string), 0, -1):
#     print(string[i])
# string = "abc"
# rev_string = string[::-1]
# for i in range(len(rev_string)):
#     print(rev_string[i])


# name = input()
# surname = input()
# second_name = input()
# print(f'{surname[0]}{name[0]}{second_name[0]}')

# s = input()
# sum = 0
# for i in range(len(s)):
#     sum += int(s[i])
# print(sum)

# string = input()
# symb = 0
# for i in range(1, len(string)):
#     if string[i - 1] == string[i]:
#         symb += 1
# print(symb)

# gl = 'ауоыиэяюе'
# glas = 0
# sogl = 'бвгджзйклмнпрстфхцчшщ'
# soglas = 0
# string = input()
# string = string.lower()
# for s in range(len(string)):
#     if string[s] in gl:
#         glas += 1
#     elif string[s] in sogl:
#         soglas += 1
# print(f'Количество гласных букв равно {glas}')
# print(f'Количество согласных букв равно {soglas}')

# #бинарная система исчисления
# n = int(input())
# binary = ''
# while n > 0:
#     binary = str(n % 2) + binary
#     n = n // 2
# print(binary if binary else '0')




# s = input()
# # общее количество символов в строке;
# print(len(s))
# # исходную строку, повторённую 3 раза;
# print(s + s + s)
# # первый символ строки;
# print(s[:1])
# # первые три символа строки;
# print(s[:3])
# # последние три символа строки;
# print(s[-3:])
# # строку в обратном порядке;
# print(s[::-1])
# # строку с удалённым первым и последним символами.
# print(s[1:-1])


# s = input()
# # третий символ этой строки;
# print(s[2:3])
# # предпоследний символ этой строки;
# print(s[-2:-1])
# # первые пять символов этой строки;
# print(s[:5])
# # всю строку, кроме последних двух символов;
# print(s[:-2])
# # все символы с чётными индексами;
# print(s[::2])
# # все символы с нечётными индексами;
# print(s[1::2])
# # все символы в обратном порядке;
# print(s[::-1])
# # все символы строки через один в обратном порядке, начиная с последнего.
# print(s[::-2])


# s = input()
# dlina = len(s)
# if dlina == 1:
#     print(s)
# elif dlina % 2 == 0 or dlina == 2:
#     dlina = int(dlina / 2)
#     print(f'{s[-dlina:]}{s[:dlina]}')
# else:
#     dlina = int((dlina - 1) / 2)
#     print(f'{s[-(dlina):]}{s[:dlina + 1]}')

# s = 'i LEARN Python LAnguaGE'

# s = 'foO BaR BAZ quX'
# print(s.capitalize())
# # Foo123#bar#

# s = 'FOO Bar 123 baz qUX'
# print(s.swapcase())
# # foo bAR 123 BAZ Qux

# s = 'the sun also rises'
# print(s.title())
# # The Sun Also Rises

# s = "what's happened to ted's IBM stock?"
# print(s.title())
# # What'S Happened To Ted'S Ibm Stock?

# s = 'FOO Bar 123 baz qUX'
# print(s.lower())
# # foo bar 123 baz qux

# s = 'FOO Bar 123 baz qUX'
# print(s.upper())
# # FOO BAR 123 BAZ QUX


# s = input()
# if 'хорош' in s.lower():
#     print('YES')
# else:
#     print('NO')

# string = input()
# col = 0
# for s in string:
#     if s == s.lower() and s.isalpha():
#         col += 1
# print(col)

# Метод count()
# s = 'foo goo moo'
# print(s.count('oo'))
# print(s.count('oo', 0, 8))  # подсчет с 0 по 7 символ
# Метод startswith()
# s = 'foobar'
# print(s.startswith('foo'))
# print(s.startswith('baz'))
# # True
# # False
# Метод endswith()
# s = 'foobar'
# print(s.endswith('bar'))
# print(s.endswith('baz'))
# # True
# # False
# Метод find()
# s = 'foo bar foo baz foo qux'
# print(s.find('foo'))
# print(s.find('bar'))
# print(s.find('qu'))
# print(s.find('python'))
# # 0
# # 4
# # 20
# # -1
# Метод rfind()
# Метод index()
# Метод rindex()
# Метод strip()
# s = '     foo bar foo baz foo qux      '
# print(s.strip())
# # foo bar foo baz foo qux
# Метод lstrip()
# Метод rstrip()
# Метод replace()
# s = 'foo bar foo baz foo qux'
# print(s.replace('foo', 'grault'))
# # grault bar grault baz grault qux
# s = 'foo bar foo baz foo qux'
# print(s.replace('foo', 'grault', 2))
# # grault bar grault baz foo qux
# s = '-+-+abc+-+-'
# print(s.strip('+-'))
# print(s.rstrip('+-'))
# print(s.lstrip('+-'))
# abc    
# -+-+abc
# abc+-+-

# s = 'aabbAAccDDaa'
# s = s.lower()
# print(s.count('a'))

# s = input()
# s = s.lower()
# print("Аденин:", s.count('а'))
# print('Гуанин:', s.count('г'))
# print('Цитозин:', s.count('ц'))
# print('Тимин:', s.count('т'))

# col = int(input())
# itog = 0
# for _ in range(col):
#     s = input()
#     summa = 0
#     for _ in range(3):
#         if s.find('11') >= 0:
#             summa += 1
#             s = s.replace('11', 'grault', 1)
#         if summa == 3:
#             itog += 1
# print(itog)

# string = input()
# summa = 0
# for s in string:
#     if s.isdigit():
#         summa += 1
# print(summa)


# s = input()
# if s.endswith('.ru') or s.endswith('.com'):
#     print('YES')
# else:
#     print('NO')


# # частовстречающийся символ
# string = input()
# s_max =''
# colmax = string.count('string[0]')
# for s in string:
#     colm = string.count(s)
#     string = string.replace(s, '')
#     if colm > colmax:
#         colmax = colm
#         s_max = s
#     elif colm == colmax:
#         colmax = colm
#         s_max = s
# print(s_max)


# string = input()
# first = string.index('h')
# allsymb = string.count('h')
# string = string.replace('h', 'a', allsymb - 1)
# last = string.index('h') + 1
# print(f'{string[:first]}{string[last:]}')


# # Метод isalnum()
# s1 = 'abc123'
# s2 = 'abc$*123'
# s3 = ''
# print(s1.isalnum())
# print(s2.isalnum())
# print(s3.isalnum())
# True
# False
# False
# s1 = 'BEEGEEK'
# s2 = '2202'
# print(s1.isalnum())
# print(s2.isalnum())
# True
# True
# # Метод isalpha()
# s1 = 'ABCabc'
# s2 = 'abc123'
# s3 = ''
# print(s1.isalpha())
# print(s2.isalpha())
# print(s3.isalpha())
# True
# False
# False
# # Метод isdigit()
# s1 = '1234567'
# s2 = 'abc123'
# s3 = ''
# print(s1.isdigit())
# print(s2.isdigit())
# print(s3.isdigit())
# True
# False
# False
# # Метод islower()
# s1 = 'abc'
# s2 = 'abc1$d'
# s3 = 'Abc1$D'
# print(s1.islower())
# print(s2.islower())
# print(s3.islower())
# True
# True
# False
# # Метод isupper()
# s1 = 'ABC'
# s2 = 'ABC1$D'
# s3 = 'Abc1$D'
# print(s1.isupper())
# print(s2.isupper())
# print(s3.isupper())
# True
# True
# False
# # Метод isspace()
# s1 = '       '
# s2 = 'abc1$d'
# print(s1.isspace())
# print(s2.isspace())
# True
# False


col = int(input())
itog = 0
for _ in range(col):
    s = input()
    summa = 0
    for _ in range(3):
        if s.find('11') >= 0:
            summa += 1
            s = s.replace('11', 'grault', 1)
        if summa == 3:
            itog += 1
print(itog)