# # Задание 1
# num1 = int(input('Введи начало диапазона: '))
# num2 = int(input('Введи конец диапазона: '))
# chet = 0
# kolchet = 0
# nechet = 0
# kolnechet = 0
# nine = 0
# kolnine = 0
# for i in range(num1,num2+1):
#     if i % 2 == 0:
#         chet += i
#         kolchet += 1
#     if i % 2 != 0:
#         nechet += i
#         kolnechet += 1
#     if i % 9 == 0:
#         nine += i
#         kolnine += 1
# print(f'сумма четных: {chet}')
# print(f'среднее арифметическое четных: {chet/kolchet}')
# print(f'сумма четных: {nechet}')
# print(f'среднее арифметическое нечетных: {nechet/kolnechet}')
# print(f'сумма кратных 9: {nine}')
# print(f'среднее арифметическое кратных 9: {nine/kolnine}')

# # Задание 2
# long = int(input('Введи длину: '))
# sym = input('Введи символ, который будем повторять: ')
# for i in range(long):
#     print(sym)

# # Задание 3
# while True:
#     sym = int(input('Введи число: '))
#     if sym == 7:
#         print('Good bye!')
#         break
#     elif sym == 0:
#         print('Number is equal to zero')
#     elif sym < 0:
#         print('Number is negative')
#     elif sym > 0:
#         print('Number is positive')

# Задание 4
text = input('Введи текст: ')
len = len(text)
ch = 0
sum = 0
for i in range(len):
    if text[i].isdigit() == True:
        ch += 1
        sum += int(text[i])
print(f'Сумма этих цифр - {sum}')