## 1
# country = ['Москва', 'Санкт-Петербург', 'Екатеринбург']
# for i in range(len(country)):
#     print(country[i])

## 2
# books = []
# j = 0
# for i in range(3):
#     b = input('Укажи любимую книгу: ')
#     books.append(b)
# while j < len(books):
#     print(books[j])
#     j += 1


## 3
user = ['Ivan', 'Petr', 'Eva']
u = input()
# if u in user:
if user.count(u) > 0:
    print('доступ разрешен')
else:
    print('доступ запрещен')