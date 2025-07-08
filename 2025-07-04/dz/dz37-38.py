# #1
# #Проверка админа
# def authorize_user(p1, p2):
#     if p1 == 'admin' and p2 == '1234':
#         return True
#     else:
#         return False

# user = input("Введите имя пользователя: ") # admin
# passwd = input("Введите пароль: ") # 1234
# result = authorize_user(user, passwd) 
# print(result) # True


# #2
# #Расчет скидки
# def apply_discount(p, s):
#     res = p - p * s / 100
#     return res

# price = int(input('Введите цену товара: '))
# discount = int(input('Введите скидку на товар: '))
# print(apply_discount(price, discount))


# #3
# # Глобальный список 
# books = []
# def add_book(book):
#     if book in books:
#         print('Такая книга уже есть в списке!')
#     else:
#         books.append(book)
#         print('Книга добавлена!')
# add_book("Преступление и наказание") 
# add_book("Война и мир") 
# add_book("Гамлет") 
# add_book("Война и мир")
# print(books)


#4
#Каталог фильмов
import json

def add_film():
    title = input('Введите название фильма: ')
    year = int(input('Введите год выпуска: '))
    genre = input('Введите жанр: ')
    with open('2025-07-04\\dz\\films.json', 'r', encoding='utf-8') as f:
        films = json.load(f)
        for f in films:
            if title == f['title']:
                print('Такой фильм уже есть в фильмотеке')
                break
        else:
            film = {
                "title": title,
                "year": year,
                "genre": genre
            }
            films.append(film)
            with open('2025-07-04\\dz\\films.json', 'w', encoding='utf-8') as f:
                json.dump(films, f, ensure_ascii=True, indent=4)
            print('Фильм добавлен!\n')

def list_film_all():
    with open('2025-07-04\\dz\\films.json', 'r', encoding='utf-8') as f:
        films = json.load(f)
        for f in films:
            print('Название - ' + f['title'] + '\n'+ 'Год выпуска - ' + str(f['year']) + '\n' + 'Жанр - ' + f['genre'] + '\n')

def list_film_for_name():
    film = input('Введите название фильма: ')
    with open('2025-07-04\\dz\\films.json', 'r', encoding='utf-8') as f:
        films = json.load(f)
        for f in films:
            if film == f['title']:
                print('Название - ' + f['title'] + '\n'+ 'Год выпуска - ' + str(f['year']) + '\n' + 'Жанр - ' + f['genre'] + '\n')
                break
        else:
            print('Такого фильма в фильмотеке нет')

while True:
    do = int(input('Выберите действие: \nДобавить фильм - 1\nПоказать все фильмы - 2\nНайти фильм - 3\nВыход - 0\n'))
    if do == 1:
        add_film()
    elif do == 2:
        list_film_all()
    elif do == 3:
        list_film_for_name()
    elif do == 0:
        print('До свидания!')
        break