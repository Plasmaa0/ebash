from textual.app import App, ComposeResult, events
from textual.widgets import DataTable, Static, Footer, Header
from textual.binding import Binding
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
    BINDINGS = [
        Binding(key="enter", action="proceed", description="Play currently selected level"),
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(key="l", action="leaderboard", description="Show the leaderboard")
    ]
    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            # Static("[green]Select level[/green] and hit [green]enter[/green]."),
            # Static("Press [red]q[/red] to [red]exit[/red]."),
            # Static("Press [cyan]l[/cyan] to see the [cyan]leaderboard[/cyan]."),
            DataTable(zebra_stripes=True),
            Footer()
        )
    
    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_columns('name','about')
        for number, row in enumerate(get_table_data(), start=1):
            label = Text(str(number), style="#B0FC38 italic")
            table.add_row(*row, label=label)
        table.cursor_type = "row"

    def action_leaderboard(self):
        self.exit('LEADERBOARD')
    
    def action_quit(self):
        self.exit()
    
    def action_proceed(self):
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