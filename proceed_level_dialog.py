from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Static


class ButtonsApp(App[str]):
    CSS_PATH = "button.css"

    def __init__(self, level_name):
        super().__init__()
        self.level_name = level_name

    def compose(self) -> ComposeResult: 
        yield Vertical(
            Static(f'You have chosen level \'{self.level_name}\'. Proceed?'),
            Horizontal(
                Button.success("Yes!"),
                Button.error("NO :("),
            )
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(event.button.variant=='success')


def proceed_to_level(name):
    app = ButtonsApp(name)
    return app.run()


if __name__=="__main__":
    proceed_to_level('123')