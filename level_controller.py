from textual.app import App, ComposeResult, events
from textual.widgets import DataTable, Static 
from textual.containers import VerticalScroll
from rich.text import Text
import os

def get_level_names():
    levels = os.listdir('levels')
    levels.remove('.gitkeep')
    return levels

def get_level_data(name:str):
    levelpath = f'levels/{name}'
    with open(f'{levelpath}/README.txt') as f:
        readme = ''.join(f.readlines())
    with open(f'{levelpath}/HINT.txt') as f:
        hint = ''.join(f.readlines())
    with open(f'{levelpath}/ABOUT.txt') as f:
        about = ''.join(f.readlines())
    return about,readme,hint

def get_table_data():
    names = get_level_names()
    table = []
    for index, name in enumerate(names):
        about,readme, hint = get_level_data(name)
        table.append((name, about))
    return table

class LevelSelectTable(App):
    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            Static("[green]Select level[/green] and hit [green]enter[/green]."),
            Static("Press [red]q[/red] to [red]exit[/red]."),
            Static("Press [cyan]l[/cyan] to see the [cyan]leaderboard[/cyan]."),
            DataTable()
        )

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns('name','about')
        for number, row in enumerate(get_table_data(), start=1):
            label = Text(str(number), style="#B0FC38 italic")
            table.add_row(*row, label=label)
        table.cursor_type = "row"

    def on_key(self, event: events.Key) -> None:
        if event.key == 'enter':
            self.key_enter()

    def key_l(self):
        self.exit('LEADERBOARD')
    
    def key_q(self):
        self.exit()
    
    def key_enter(self):
        table = self.query_one(DataTable)
        # exit(row_key)
        row = table.get_row(table.coordinate_to_cell_key(table.cursor_coordinate).row_key)
        level_name = row[0]
        self.exit(level_name)

def select_level():
    app = LevelSelectTable()
    return app.run()


# if __name__ == "__main__":
#     app = LevelSelectTable()
#     app.run()