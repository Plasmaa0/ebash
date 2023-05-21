from textual.app import App, ComposeResult
from textual.widgets import Tree, Static, Footer
from textual.containers import VerticalScroll
from textual.binding import Binding
import json

def read_leaderboard():
    with open('rating.json', 'r') as f:
        rating = json.load(f)
    return rating

def write_leaderboard(rating):
    with open('rating.json', 'w') as f:
            json.dump(rating, f, ensure_ascii=False, indent=4)

def add_to_leaderboard(player, level):
    print(f'adding {level} to {player}\'s achievements')
    rating = read_leaderboard()
    if player not in rating.keys():
        rating[player] = [0, []]
    if level not in rating[player][1]:
        rating[player][0]+=1
        rating[player][1].append(level)
    else:
        print(f'{player} have already completed level {level}')
    write_leaderboard(rating)

class TreeApp(App):
    BINDINGS = [
        Binding(key="escape", action="quit", description="Close leaderboard table"),
    ]
    
    def __init__(self, player_name):
        super().__init__()
        self.selected_player_name = player_name
        
    def compose(self) -> ComposeResult:
        tree: Tree[dict] = Tree("Leaderboard")
        tree.root.expand()
        tree.root.allow_expand = False
        rating = read_leaderboard()
        sorted_rating = sorted([[name, rating[name]] for name in rating.keys()], key=lambda x: x[1][0], reverse=True)
        for player_name, player_rating in sorted_rating:
            modifier = '[magenta]' if player_name == self.selected_player_name else ''
            player_entry = tree.root.add(f'{player_rating[0]} {modifier}{player_name}', expand=False,allow_expand=len(player_rating[1])>0)
            for completed_level in player_rating[1]:
                player_entry.add_leaf(completed_level)
        yield VerticalScroll(
            # Static("[green bold]Press escape key to exit"),
            tree,
            Footer()
        )

    def action_quit(self) -> None:
        self.exit()

if __name__ == "__main__":
    app = TreeApp('plasmaa0')
    app.run()

def show_leaderboard(player_name):
    app = TreeApp('plasmaa0')
    app.run()