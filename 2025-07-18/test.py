# answer = input()
# # чекаем введенные пользователем символы
# answer = answer.split('-')
# tovar = answer[0].strip()
# price = answer[1].strip()
# if not price.isdigit():
#     print('Вы ввели не только цифры')
# print(tovar,price)
# # if not answer.isdigit():
# #     print('Вы ввели не только цифры')

# import json
# user_id = int(input())
# with open('2025-07-15\\buy.json', 'r', encoding='utf-8') as f:
#         data = json.load(f)
#         # send_message(user_id, 'Список товаров')
#         for d in data:
            
#             if d['user_id'] == user_id:
#                 mess = d['name'] + ' ' + str(d['price'])
#                 print(user_id, mess)
# import json
# user_for_del = str(input('Введите имя удаляемого сотрудника\n'))
# print(user_for_del)
# with open('2025-07-15\\buy.json', 'r', encoding='utf-8') as f:  # открыли файл
#     data = json.load(f)  # загнали все из файла в переменную
# minimal = 0
# for txt in data['personal']:
#     print('Запись №:', minimal)
#     print(txt['name'], ':', txt['salary'])
#     if txt['name'] == user_for_del:
#       print('Запись будет удалена')
#       data['personal'].pop(minimal)
#     else:
#       None
#     minimal = minimal + 1
# print('Итоговый результат: ')
# print(data)
# print('А теперь записываем итоговый файл')
# with open('2025-07-15\\buy.json', 'w', encoding='utf8') as outfile:
#     json.dump(data, outfile, ensure_ascii=False, indent=2)
import json
with open('2025-07-15\\buy.json', 'r', encoding='utf-8') as f:
    tovars = json.load(f)
new_tovars = []
print(tovars)
for w in tovars:
    if w['name'] != 'dsad' and w['user_id'] != 23:
        new_tovars.append(w)
    # with open('2025-07-15\\buy.json', 'w', encoding='utf-8') as f:
    #     json.dump(new_tovars, f, ensure_ascii=True, indent=4)
print('----------------------------------------------')
print(new_tovars)