from textual.app import App, ComposeResult, events
from textual.widgets import DataTable, Footer, Button
from textual.binding import Binding
from textual.containers import VerticalScroll, Horizontal
from rich.text import Text
import os
from quit_screen import QuitScreen

def get_level_names():
    levels = os.listdir('levels')
    levels.sort()
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
        if name[:3].isdigit() and name[3]=='_':
            name = name[4:]
        name = name.replace('_', ' ')
        table.append((name, about))
    return table

class LevelSelectTable(App):
    CSS_PATH = "button.css"
    BINDINGS = [
        Binding(key="q", action="quit", description="Quit the app"),
        Binding(key="enter", action="proceed", description="Play currently selected level"),
        Binding(key="l", action="leaderboard", description="Show the leaderboard")
    ]
    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            # Static("[green]Select level[/green] and hit [green]enter[/green]."),
            # Static("Press [red]q[/red] to [red]exit[/red]."),
            # Static("Press [cyan]l[/cyan] to see the [cyan]leaderboard[/cyan]."),
            DataTable(zebra_stripes=True),
            Horizontal(
                Button.success("Начать!",name='start'),
                Button("Рейтинг", variant="primary",name='rating'),
                Button.error("Выйти", name='exit')
            ),
            Footer()
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.name == 'start':
            self.action_proceed()
        if event.button.name == 'rating':
            self.action_leaderboard()
        if event.button.name == 'exit':
            self.action_quit()
    
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
        self.push_screen(QuitScreen())
    
    def action_proceed(self):
        table = self.query_one(DataTable)
        row_index= str(table.cursor_coordinate.row+1)
        row_str = row_index.rjust(3,'0')
        for file in os.listdir('levels'):
            if row_str in file:
                self.exit(file)
                return
        self.exit('ERROR')

def select_level():
    app = LevelSelectTable()
    return app.run()


if __name__ == "__main__":
    app = LevelSelectTable()
    result = app.run()
    print(result)