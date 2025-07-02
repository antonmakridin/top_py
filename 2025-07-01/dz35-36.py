# #1
# def place(country, capital):
#     print(f'страна: {country}, столица: {capital}')
# co = input('Введите страну: ')
# ca = input('Введите столицу: ')
# print(place(co, ca))


# #2
# def summa_chet(a, b):
#     sum = 0
#     for i in range(a, b + 1):
#         if i %2 == 0:
#             sum += i
#     return sum
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# print('Сумма четных:', summa_chet(a, b))


# #3
# def perimetr(a, b):
#     p = 2 * a + 2 * b
#     return p
# a = int(input('Введите одну сторону прямоугольника: '))
# b = int(input('Введите другую сторону прямоугольника: '))
# print('Периметр равен:', perimetr(a, b))


# #4
# def minimum(numbers):
#     min1 = numbers[0]
#     for num in numbers:
#         if num < min1:
#             min1 = num
#     return min1
# numbers = [4, 12, 3, 43, 4, 100, 2]
# print('Минимальное число из списка:', minimum(numbers))


#5
def minimum(numbers):
    chet = []
    for num in numbers:
        if num % 2 == 0:
            chet.append(num)
    return chet
numbers = [4, 12, 3, 43, 4, 100, 2]
print('Четные числа:', minimum(numbers))