# #1
# numbers_1 = [1,2,3,4,5, -2]
# numbers_2 = [7, -1, 4, 5]
# numbers_3 = []
# numbers_temp = numbers_1 + numbers_2
# for i in range(len(numbers_temp)):
#     if numbers_temp[i] > 0:
#         numbers_3.append(numbers_temp[i])
# print(numbers_3)

#2
# sum = 0
# pol = 0
# colpol = 0
# numbers = [43, 5, -1, 4, 12, -4]
# for i in range(len(numbers)):
#     sum += numbers[i]
#     if numbers[i] > 0:
#         pol += numbers[i]
#         colpol += 1
# print(sum / len(numbers), pol / colpol, sep='\n')

# #3
# numbers = [43, 5, -1, 4, 12, -4, 20, 4 ]
# ch = []
# nech = []
# otr = []
# pol = []
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         ch.append(numbers[i])
#     if numbers[i] % 2 != 0:
#         nech.append(numbers[i])
#     if numbers[i] < 0:
#         otr.append(numbers[i])
#     if numbers[i] > 0:
#         pol.append(numbers[i])
# print(ch, nech, otr, pol, sep='\n')

#4
# text = "Спасение наше друг в друге в божественно замкнутом круге куда посторонним нет входа где третье лицо лишь природа."
# print(len(text.split()))

#5
print('Список покупок')
list = []
while True:
    do = str.capitalize(str.lower(input('Введите товар: ')))
    if do != "Выход":
        if list.count(do) == 0:
            list.append(do)
        else:
            print(f"Товар '{do}' уже есть в списке.")
    if do == "Выход":
        print('Ваш список покупок:')
        for i in range(len(list)):
            print(f'{i + 1}. {list[i]}')
        break