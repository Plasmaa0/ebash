from textual.app import App, ComposeResult
from textual.widgets import MarkdownViewer, Static
from textual.containers import VerticalScroll
from level_controller import get_level_data

EXAMPLE_MARKDOWN = """\
# Markdown Document

This is an example of Textual's `Markdown` widget.

## Features

Markdown syntax and extensions are supported.

- Typography *emphasis*, **strong**, `inline code` etc.
- Headers
- Lists (bullet and ordered)
- Syntax highlighted code blocks
- Tables!
"""


class MarkdownExampleApp(App):
    def __init__(self, level_name):
        super().__init__()
        self.level_name = level_name
    
    def on_key(self, event) -> None:
        self.exit()
    
    def compose(self) -> ComposeResult:
        about,readme,hint=get_level_data(self.level_name)
        MARKDOWN = f"""\
### ABOUT

_{about}_

# TASK

{readme}

## Useful commands

* `check` - check if the quest completed
* `hint` - display hint
* `stop` - stop the quest
* `readme` - display text of the task

"""
        yield VerticalScroll(
            Static("[red bold]Press any key to continue"),
            MarkdownViewer(MARKDOWN, show_table_of_contents=False)
        )

def show_level_info(level_name):
    app = MarkdownExampleApp(level_name)
    app.run()