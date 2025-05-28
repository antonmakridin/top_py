# #1
# question = [['Столица Италии', 'Рим'], ['Длинная река в Египте', 'Нил'], ['Самый большой океан', 'Тихий']]
# for q in question:
#     otvet = True
#     o = input(q[0] + ' ').capitalize()
#     if o != q[1]:
#         otvet = False
#         print('Неправильный ответ')
#     else:
#         print('Правильный ответ')


# #2
# numbers = [12, 34, 2, 3, 46]
# max1 = numbers[0]
# for num in numbers:
#     if num > max1:
#         max1 = num
# print(max1)


# #3
menu = ["Салат с курицей", "Веганский бургер", "Паста с грибами", "Бифштекс", "Рыбный суп"]
not_vegan_keywords = ["куриц", "бифштекс", "рыб", "мяс"]
for n in not_vegan_keywords:
    for m in menu:
        if m.count(n) != 0 or m.count(n.lower()) != 0 or m.count(n.capitalize()) != 0:
            menu.remove(m)
print(menu)