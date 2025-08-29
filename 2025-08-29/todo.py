import os
import json
from rich.console import Console
from rich.style import Style
from rich.table import Table
from abc import ABC, abstractmethod

class Abstractview(ABC):
    
    @abstractmethod
    def print(self):
        pass

    def print_tasks(self):
        pass

class RichView():

    def print(self, text: str):
        console = Console()
        style = Style(color='blue', bgcolor='yellow')
        console.print(text, style=style)

    def print_tasks(self, tasks: list):
        console = Console()
        table = Table(title="Список дел")
        table.add_column("№", style="cyan")
        table.add_column("Название", style="green")

        for i, name in enumerate(tasks, start=1):
            table.add_row(str(i), name)
        console.print(table)

class BasicView():

    def print(self,text: str):
        print(text)
    
    def print_tasks(self, tasks: list):
        for task in tasks:
            print(task)

class DB:
    def __init__(self, filename):
        self.filename = filename

    def add_task(self, task_name):
        tasks = self.read()
        tasks.append(task_name)
        self.write(tasks)
    
    def write(self, tasks):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, ensure_ascii=False)
    
    def read(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r', encoding='utf-8') as f:
            return json.load(f)


class ToDo:
    def __init__(self, db: DB, view: RichView):
        self.db = db
        self.view = view
    
    def add_task(self):
        task_name = input('Введи задачу: ')
        self.db.add_task(task_name)
        self.view.print('Задача добавлена')

    def list_task(self):
        tasks = self.db.read()
        self.view.print_tasks(tasks)

# Экземпляр класса базы данных
db = DB('2025-08-29\\tasks.json')
# база передается в todo
rich_view = RichView()
basic_view = BasicView()


user = int(input('1 - базовая версия, 2 - платная версия: '))
if user == 1:
    todo = ToDo(db, basic_view)
elif user == 2:
    todo = ToDo(db, rich_view)

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
