import sqlite3

db_path = "2025-10-07\\dz\\school.db"

def get_student(name):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM student WHERE name = ?", (name, ))
        res = cur.fetchone()
        return res

def add_student(user_name, user_age, user_class):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO student (name, age, class) VALUES (?, ?, ?)", (user_name, user_age, user_class))
        conn.commit()
    
def check_student(user_name, user_age, user_class):
    with sqlite3.connect(db_path) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM student WHERE name = ? AND age = ? AND class = ?", (user_name, int(user_age), user_class))
        res = cur.fetchone()
        return res

while True:
    do = int(input('Выбери действие: \n 1. Найти студента \n 2. Добавить студента \n 3. Выход \n'))
    if do == 1:
        name = input('Введите имя и фамилию студента: ')
        user = get_student(name)
        if user:
            print(f'\n{user[1]}, Возраст {user[2]}, Класс {user[3]}\n')
    elif do == 2:
        name = input('Введите имя и фамилию студента: ')
        age = int(input('Введите возраст студента: '))
        class_student = input('Введите класс студента: ')
        checktask = check_student(name, age, class_student)
        if checktask:
            print('\nТакой студент уже есть.\n')
        else:
            addstudent = add_student(name, age, class_student)
            print('\nСтудент добавлен\n')
    elif do == 3:
        print('\nДо свидания!')
        break
