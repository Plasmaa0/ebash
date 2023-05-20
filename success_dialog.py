from textual.app import App, ComposeResult
from textual.widgets import Markdown
from textual.containers import Vertical
from level_controller import get_level_data

class SuccessDialog(App):
    CSS_PATH = "button.css"
    def __init__(self, level_name):
        super().__init__()
        self.level_name = level_name
    
    def on_key(self, event) -> None:
        self.exit()
    
    def compose(self) -> ComposeResult:
        yield Markdown(f"# You have successfully completed level '{self.level_name}'!\n## Press any key to continue", classes="color:green")

def success_dialog(level_name):
    app = SuccessDialog('touch_command')
    app.run()
    
if __name__=="__main__":
    success_dialog('123')