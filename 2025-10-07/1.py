import sqlite3

# создание подключения
conn = sqlite3.connect("2025-10-07\\db.db")

# создание курсора для транзацкий-запросов
cur = conn.cursor()

# Создаём таблицу (если нет)
cur.execute("""CREATE TABLE IF NOT EXISTS users 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL)""")

cur.execute("""CREATE TABLE IF NOT EXISTS tasks 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id) )""")

# добавляем данные
# cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 25))

# Сохраняем изменения
conn.commit()

# добавляем данные
cur.execute("INSERT INTO users (name) VALUES ('Alice')")
conn.commit()


# Закрываем соединение
conn.close()