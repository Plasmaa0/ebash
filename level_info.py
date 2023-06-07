from textual.app import App, ComposeResult
from textual.widgets import MarkdownViewer,Markdown, Static, Footer, Button
from textual.containers import VerticalScroll, Grid
from textual.binding import Binding
from textual.screen import Screen
from textual import events
from level_controller import get_level_data


class HelpWindow(Screen):
    def compose(self) -> ComposeResult:
        help_md = '''\
        ## Useful commands

        * `check` - check if the quest completed
        * `hint` - display hint
        * `stop` - stop the quest
        * `readme` - display text of the task    
        '''
        # yield Button("123123123")
        yield Grid(Markdown(help_md))
    
    def key_q(self):
        self.app.pop_screen()
        
        
class MarkdownExampleApp(App):
    BINDINGS=[
        Binding("*", 'proceed','Press any key to continue'),
        Binding(
            key="question_mark",
            action="help",
            description="Show help screen",
            key_display="?",
        )
    ]
    def __init__(self, level_name):
        super().__init__()
        self.level_name = level_name
    
    def action_help(self):
        self.app.push_screen(HelpWindow())
    
    def on_key(self, event:events.Key) -> None:
        if event.key != "question_mark":
            self.exit()
    
    def compose(self) -> ComposeResult:
        about,readme,hint=get_level_data(self.level_name)
        MARKDOWN = f"""\
### ABOUT

_{about.strip()}_

# TASK

{readme}
"""
        yield VerticalScroll(
            # Static("[red bold]Press any key to continue"),
            MarkdownViewer(MARKDOWN, show_table_of_contents=False),
            Footer()
        )

def show_level_info(level_name):
    app = MarkdownExampleApp(level_name)
    app.run()
    
if __name__ == '__main__':
    show_level_info('006_cmake_program')