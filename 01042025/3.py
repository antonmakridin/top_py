# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# print(f'Сумма чисел: {a + b}. \nРазность чисел: {a-b}')

# total = int(input('Введи сумму покупки: '))
# if total > 1000:
#     total -= total*0.1
#     print(f'Итоговая сумма покупки: {total}')

# chislo = int(input('Введи число: '))
# if chislo % 2 == 0:
#     print('Число четное')

# temp = int(input('Введи температуру за бортом: '))
# if temp > 30 or temp < 0:
#     print('Экстремальные условия')
# else:
#     print('нормально')

# rubl = int(input('Введи сумму для перевода: '))
# valuta = input('Введи валюту для перевода (доступно: USD, EUR): ')
# usd = 86
# eur = 94
# if valuta == 'USD':
#     print(f'Вы получите: {rubl/usd}')
# elif valuta == 'EUR':
#     print(f'Вы получите: {rubl/eur}')

# temp = int(input('Введи температуру за бортом: '))
# if temp < 0:
#     print('На улице холодно')
# elif temp >=0 and temp <=25:
#     print ('На улице комфортно')
# elif temp > 25:
#     print('На улице жарко')

# old = int(input('Введи свой возраст: '))
# bilet = input('У тебя есть билет? (да/нет): ')

# if old >= 18 and old <= 50 and bilet == 'да':
#     print('Регистрация успешна')
# else:
#     print('Регистрация невозможна')

# vopros1 = int(input('сколько будет 6+8: '))
# vopros2 = input('кто президент России: ')
# vopros3 = int(input('укажи примерное расстояние от Земли до Луны (тыс. км): '))

# if vopros1 == 14 and vopros2 == 'Путин' and vopros3 >= 380:
#     print('3 балла! Да ты эрудит!')
# elif (vopros1 == 14 and vopros2 == 'Путин' and vopros3 < 380) or (vopros1 == 14 and vopros2 != 'Путин' and vopros3 >= 380) or (vopros1 != 14 and vopros2 == 'Путин' and vopros3 >= 380):
#     print('2 балла')
# elif (vopros1 == 14 and vopros2 != 'Путин' and vopros3 < 380) or (vopros1 != 14 and vopros2 != 'Путин' and vopros3 >= 380):
#     print('1 балл')
# elif vopros1 != 14 and vopros2 != 'Путин' and vopros3 < 380:
#     print('0 баллов')

vopros1 = int(input('сколько будет 6+8: '))
vopros2 = input('кто президент России: ')
vopros3 = int(input('укажи примерное расстояние от Земли до Луны (тыс. км): '))
n=0
if vopros1 == 14:
    n += 1
if vopros2 == 'Путин':
    n += 1
if vopros3 >= 380:
    n += 1
print(f'Количество баллов: {n}')