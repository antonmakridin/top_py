import os
import json

class DB:
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, tasks):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False)
    
    def read(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)


class ToDo:
    def __init__(self, db):
        self.db = db
    
    def add_task(self):
        task_name = input('Введи задачу: ')
        tasks = self.db.read()
        tasks.append(task_name)
        self.db.write(tasks)
        print('Задача добавлена')

    def list_task(self):
        print('Твой список дел:')
        for index, d in enumerate(self.tasks, start=1):
           print(f"{index}. {d}")

# Экземпляр класса базыданных
db = DB('2025-08-26\\tasks.json')
# база передается в todo
todo = ToDo(db)

while True:
    print('\nВыбери действие\n')
    print('1 - добавить дело')
    print('2 - посмотреть дела')
    print('3 - выход')
    action = input('Вводи: ')
    if action == '1':
        # вызвать метод добавления дела
        todo.add_task()

    elif action == '2':
        # вызваем метод просмотра дел
        todo.list_task()

    elif action == '3':
        print('До свидания')
        break
