import os
import tabulate
import pexpect
import shutil
import random
from level_controller import select_level as select_level_table, get_level_data
from proceed_level_dialog import proceed_to_level
from level_info import show_level_info
from success_dialog import success_dialog
from leaderboard_table import show_leaderboard, add_to_leaderboard

def exit_with_error(errorstr):
    print("Something went wrong! "+errorstr)
    exit(1)


def play_level(player_name,name):
    show_level_info(name)
    bash = pexpect.spawn("bash")
    success_exit_code = random.randint(5,100)
    # print('setting exit code to',success_exit_code)
    bash.sendline(f"source test.sh {name} {success_exit_code};history -w;history -c;clear;readme;")
    bash.interact()
    exit_code = bash.wait()
    # print(f"code {exit_code}")
    if exit_code == success_exit_code:
        success_dialog(name)
        add_to_leaderboard(player_name, name)
        
def select_level(player_name):
    level_name = select_level_table()
    if level_name is None:
        exit()
    if level_name == "LEADERBOARD":
        show_leaderboard(player_name)
    elif proceed_to_level(level_name):
        play_level(player_name,level_name)


def main():
    player_name = os.environ.get('USER')
    print(f'Hello {player_name}!')
    while True:
        select_level(player_name)

if __name__ == "__main__":
    main()

# with open('levels.json', 'r') as f:
#     levels = json.load(f)
#     entries = []
#     for index, level in enumerate(levels):
#         entry = str(index)+' '
#         entry += ('да' if level['completed'] else 'нет') + ' '
#         entry += '"'+level['name'] + '" '
#         entry += '"'+level['description'] + '" '
#         entry += level['uuid']
#         entries.append(entry)
#     result =  ' '.join(entries)
#     print(result)
