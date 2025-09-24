# #1
# a = 7
# b = 10
# print(f'Периметр прямоугольника со сторонами {a} и {b} равен {a * b}')


# #2
# t = int(input('Укажите время в часах: '))
# v = int(input('Укажите скорость в км/ч: '))
# print(f'Вы преодолели расстояние: {t * v} километров')


# #3
# score = int(input("Введите количество набранных баллов (от 0 до 100): "))
# if 90 <= score <= 100:
#     print("отлично")
# elif 70 <= score <= 89:
#     print("хорошо")
# elif 50 <= score <= 69:
#     print("удовлетворительно")
# elif 0 <= score < 50:
#     print("нужно постараться")
# else:
#     print("Ошибка: введите число от 0 до 100")


# #4
# for number in range(2, 21, 2):
#     print(number)
# #или
# for number in range(2, 21):
#     if number % 2 == 0:
#         print(number)


# #5
# s = 'a1s2d3f4g5h6j7k8l9'
# count = 0
# for char in s:
#     if char.isalpha():
#         count += 1
# print(count)


# #6
# s1 = 'пмркевытлд'
# s2 = 'ри ак еа'
# itog = s1 + s2
# result = ""
# for i in range(0, len(itog), 3):
#     result += itog[i]
# print(result)


#7
l = ['3', 'b', '7', '12', 'a', '4']
numbers = []
for item in l:
    if item.isdigit():
        numbers.append(int(item))
proiz = 1
for num in numbers:
    proiz *= num
print("Числа:", numbers)
print("Произведение:", proiz)