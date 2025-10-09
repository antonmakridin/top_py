import sqlite3


def get_user(name):
    with sqlite3.connect("2025-10-07\\db.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE name = ?", (name, ))
        # cur.execute("INSERT INTO users (name) VALUES (?)", (name, ))
        res = cur.fetchone()
        return res

def add_task(user_id, task_name):
    with sqlite3.connect("2025-10-07\\db.db") as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO tasks (name, user_id) VALUES (?, ?)", (task_name, user_id, ))
        conn.commit()
    
def check_task(user_id, task_name):
    with sqlite3.connect("2025-10-07\\db.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE user_id = ? and name = ?", (user_id, task_name))
        # cur.execute("INSERT INTO users (name) VALUES (?)", (name, ))
        res = cur.fetchone()
        return res



# while True:
name = input('Введи имя: ')
# идем в базу, проверяем такого пользователя
user = get_user(name)
if user:
    print(f'Имя {user[1]} выбрано')
    while True:
        task = input('Введи задачу: ')
        if task == 'Достаточно':
            break
        checktask = check_task(user[0], task)
        if checktask:
            print('Такая задача уже есть')
        else:
            addtask = add_task(user[0], task)
            print('Задача добавлена')
else:
    print('')