##1
# n, s = input(), input()
# print(n, s, '- рады снова видеть вас в академии!')

##2
# import math
# r = float(input())
# print(math.pi * r * math.pow(r, 2))

##3
# for i in range(0, 100, 3):
#     print(i)
# for i in range(0, 100):
#     if i % 3 == 0:
#         print(i)

##4
sum = 0
# for i in range(5):
#     p, col = float(input('Введи цену товара: ')), int(input('Введи количество товара: '))
#     if p > 0 and col > 0:
#         s = p * col
#         sum += s
#     else:
#         print('Невалидные данные')
# print(sum)

##5
# from random import randint
# q = input('Введи вопрос: ')
# if randint(1,2) == 1:
#     print('да')
# else:
#     print('нет')

##6
# o = int(input())
# if 8 < o <= 10:
#     print('здорово! Вы хорошо отдохнули')
# elif 6 < o <= 8:
#     print('неплохой результат')
# elif 4 < o <= 6:
#     print('вам бы еще недельку, да?')
# elif 0 < o <= 4:
#     print('бывает, все впереди.')
# else:
#     print('ошибка ввода')


##7
# print('Обменник')
# while True:
#     ch1 = int(input('Введи количество рублей для перевода: '))
#     do = int(input('Выбери действие: \n 1. Перевести в доллары \n 2. Перевести в евро \n 3. Перевести в юани \n 4. Выход \n'))
#     if do == 1:
#         print(f'Вы получите {ch1/80.7} долларов')
#     elif do == 2:
#         print(f'Вы получите {ch1/90.03} евро')
#     elif do == 3:
#         print(f'Вы получите {ch1/11.20} юаней')
#     elif do == 4:
#         print('До свидания! Приходите еще в наш обменник.')
#         break

##8
# country = ['Индия', 'Австралия', 'Италия']
# for i in range(3):
#     print(country[i])

##9
# eda = []
# j = 0
# for i in range(3):
#     u = input('Что ты купил на ужин? ')
#     eda.append(u)
# while j < len(eda):
#     print(eda[j])
#     j += 1


##10
from random import randint
question = ['3+2', '5+7', '4*5']
answers = ['5', '12', '20']
q = randint(0,len(question)-1)
print('напиши результат примера:', question[q])
for i in range(3):
    o = input('твой ответ: ')
    if o == answers[q]:
        print('Верно')
        break
