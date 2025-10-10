import sqlite3


def get_user(name):
    with sqlite3.connect("2025-10-07\\db.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE name = ?", (name, ))
        res = cur.fetchone()
        return res

def add_user(user_name):
    with sqlite3.connect("2025-10-07\\db.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("INSERT INTO users (name) VALUES (?)", (user_name, ))
        conn.commit()
    
def check_user(user_name):
    with sqlite3.connect("2025-10-07\\db.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE name = ?", (user_name, ))
        res = cur.fetchone()
        return res

def add_task(user_id, task_name):
    with sqlite3.connect("2025-10-07\\db.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("INSERT INTO tasks (name, user_id) VALUES (?, ?)", (task_name, user_id, ))
        conn.commit()

def update_task(user_id, task_name):
    with sqlite3.connect("2025-10-07\\db.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("UPDATE tasks SET status = '1' WHERE name = (?) AND user_id = (?)", (task_name, user_id, ))
        conn.commit()
    
def check_task(user_id, task_name):
    with sqlite3.connect("2025-10-07\\db.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE user_id = ? AND name = ? AND status = 0", (user_id, task_name))
        res = cur.fetchone()
        return res
    
def get_tasks(user_id):
    with sqlite3.connect("2025-10-07\\db.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE user_id = ?  AND status = 0", (user_id, ))
        res = cur.fetchall()
        return res
    
def get_do_tasks(user_id):
    with sqlite3.connect("2025-10-07\\db.db") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM tasks WHERE user_id = ?  AND status = 1", (user_id, ))
        res = cur.fetchall()
        return res

while True:
    do = int(input('Выбери действие: \n 1. авторизоваться \n 2. добавить пользователя \n 3. Выход \n'))
    # while True:
    if do == 1:
        name = input('Введи имя: ')
        # идем в базу, проверяем такого пользователя
        user = get_user(name)
        if user:
            user = dict(user)
            print(f'Имя {user['name']} выбрано')
            while True:
                do_user = int(input('Выбери действие: \n 1. добавить задачу \n 2. вывести невыполненные задачи \n 3. вывести выполненные задачи \n 4. выполнить задачу \n 5. Выход \n'))
                if do_user == 1:
                    task = input('Введи задачу: ')
                    if task == 'й' or task == 'q':
                        break
                    checktask = check_task(int(user['id']), task)
                    if checktask:
                        print('Такая задача уже есть')
                    else:
                        addtask = add_task(user['id'], task)
                        print('Задача добавлена')
                elif do_user == 2:
                    gettasks = get_tasks(user['id'])
                    for i, task in enumerate(gettasks, 1):
                        print(f'{i}. {task['name']}')
                elif do_user == 3:
                    gettasks = get_do_tasks(user['id'])
                    for i, task in enumerate(gettasks, 1):
                        print(f'{i}. {task['name']}')
                elif do_user == 4:
                    gettasks = get_tasks(user['id'])
                    for i, task in enumerate(gettasks, 1):
                        print(f'{i}. {task['name']}')
                    do_dask = input('Введи название задачи для выполнения: ')
                    if do_dask == 'й' or do_dask == 'q':
                        break
                    checktask = check_task(int(user['id']), do_dask)
                    if checktask:
                        updatetask = update_task(int(user['id']), do_dask)
                    else:
                        print('Такой задачи нет')
                elif do_user == 5:
                    break
        else:
            print('нужна авторизация')
    elif do == 2:
        name = input('Введи имя: ')
        checkuser = check_user(name)
        if checkuser:
            print('Пользователь с таким именем уже есть')
        else:
            adduser = add_user(name)
            print('Пользователь добавлен')
    elif do == 3:
        break