from rich.console import Console
from rich.style import Style
from rich.table import Table


class RichView():

    def print(self,text):
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


view = RichView()
view.print('Hello')
view.print_tasks(['Первая задача', 'Вторая задача', 'Третья задача'])
