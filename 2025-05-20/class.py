# products = ['яблоко', 'апельсин' , 'молоко']
# for product in ['яблоко', 'молоко']:
#     print(product)

##1
# numbers_1 = [40,2,3,1,5]
# numbers_2 = []
# for i in range(len(numbers_1)):
#     if numbers_1[i] % 2 == 0:
#         numbers_2.append(numbers_1[i])
# print(numbers_2)

##2
# numbers = [43,5,-1,4,12,17,-2]
# min = numbers[0]
# for i in range(len(numbers)-1):
#     if numbers[i+1] < min:
#         min = numbers[i+1]
# print(min)

##3
# otr = 0
# ch = 0
# nech = 0
# krat = 1
# numbers = [12, 4, 5, -3, 12, -6, 1, 7, 2]
# for i in range(len(numbers)):
#     if numbers[i] < 0:
#         otr += numbers[i]
#     if numbers[i] % 2 == 0:
#         ch += numbers[i]
#     if numbers[i] % 2 != 0:
#         nech += numbers[i]
#     if i % 3 == 0:
#         krat *= numbers[i]
# print(otr,ch,nech,krat,sep='\n')

# from random import randint
# numbers = []
# for j in range(9):
#     num = randint(-50, 50)
#     numbers.append(num)
# print(numbers)
# for i in range(len(numbers)):
#     if numbers[i] < 0:
#         otr += numbers[i]
#     elif numbers[i] % 2 == 0:
#         ch += numbers[i]
#     elif numbers[i] % 2 != 0:
#         nech += numbers[i]
#     elif i % 3 == 0:
#         krat += numbers[i]
# print(otr,ch,nech,krat,sep='\n')



##4
# question = []
# answers = []
# col = int(input('укажите количество вопросов викторины: '))
# for i in range(col):
#     q = input(f'Введите вопрос #{i+1}: ')
#     question.append(q)
# for i in range(col):
#     a = input(f'Введите ответ #{i+1}: ')
#     answers.append(a)
# #print(question,answers,sep='\n')
# print(f'question = {question}')
# print(f'answers = {answers}')

##5
# s = input('Введите предложение: ')
# print(len(s.split()))

##6
# s = input('Введите предложение: ')
# # s = 'В1центре1Галактики1находится1сверхмассивная1чёрная1дыра'
# s = s.split('1')
# s = ' '.join(s)
# print(s)

##7
# text = 'Для того чтобы изучить программирование нужно всего лишь изучать его и все'
# secret = ['программирование', 'изучать', 'его']
# t = text.split()
# for j in range(len(secret)):
#     for i in range(len(t)):
#         if t[i] == secret[j]:
#             t[i] = '*'
# t = ' '.join(t)
# print(t)

##8
# countries = ['Италия', 'Индия', 'Россия', 'США', 'Китай', 'Нидерланды'] 
# people = [58966453, 1434998000, 146150789, 341169410, 1409670000, 17967505]
# min = people[0]
# j = 0
# for i in range(len(people)-1):
#     if people[i+1] < min:
#         min = people[i+1]
#         j = i + 1
# print(f'Страна с населением - {min} является {countries[j]}')

##9
# print('To-Do List')
# list = []
# while True:
#     do = int(input('Выбери действие: \n 1. Добавление задачи \n 2. Удаление задачи \n 3. Просмотр списка \n 4. Выход \n'))
#     if do == 1:
#         t = input('Введите новую задачу: ')
#         list.append(t)
#     elif do == 2:
#         num = int(input(f'Укажите номер задачи для удаления (максимум {len(list)}): '))
#         if num != '':
#             num = num - 1
#             list.pop(num)
#         else:
#             print('Не указан номер задачи')
#     elif do == 3:
#         for i in range(len(list)):
#             print(f'{i + 1}. {list[i]}')
#     elif do == 4:
#         print('До свидания!')
#         break