import os
import tabulate
import pexpect
import shutil
import random
import json

SUCCESS_EXIT_STATUS = 44

def exit_with_error(errorstr):
    print("Something went wrong! "+errorstr)
    exit(1)

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

def play_level(player_name,name):
    about, readme, hint = get_level_data(name)
    table = [
        ['About', about],
        ['Readme', readme]
    ]
    cols, rows = shutil.get_terminal_size((80, 20))
    table_str = tabulate.tabulate(table,tablefmt="grid",maxcolwidths=[7,cols-7])
    print(table_str)
    bash = pexpect.spawn("bash")
    success_exit_code = random.randint(5,100)
    # print('setting exit code to',success_exit_code)
    bash.sendline(f"source test.sh {name} {success_exit_code}")
    bash.interact()
    exit_code = bash.wait()
    # print(f"code {exit_code}")
    if exit_code == success_exit_code:
        print("Succcess!!")
        add_to_leaderboard(player_name, name)

def select_level(player_name):
    names = get_level_names()
    table = []
    for index, name in enumerate(names):
        about,readme, hint = get_level_data(name)
        table.append([index, name, about])
    headers = ['i','name','about']
    cols, rows = shutil.get_terminal_size((80, 20))
    table_str = tabulate.tabulate(table,headers=headers,tablefmt="grid",maxcolwidths=[5,30,cols-35])
    print(table_str)
    try:
        choice = input('Select single level from above (or "exit"): ')
        if choice == 'exit':
            raise SystemExit(f"Bye {player_name}!")
        else:
            choice = int(choice)
    except Exception as e:
        if Exception is SystemExit:
            exit(0)
        exit_with_error('Wrong input')
    else:
        if not (0<=choice and choice<len(names)):
            exit_with_error('Wrong index')
        proceed = input(f'You have chosen level \'{names[choice]}\'. Proceed? [Y/n]: ') in ['Y', 'y','']
        if proceed:
            play_level(player_name,names[choice])

def add_to_leaderboard(player, level):
    print(f'adding {level} to {player}\'s achievements')
    with open('rating.json', 'r') as f:
        rating = json.load(f)
    if player not in rating.keys():
        rating[player] = [0, []]
    if level not in rating[player][1]:
        rating[player][0]+=1
        rating[player][1].append(level)
    else:
        print(f'{player_name} have already completed level {level}')
    with open('rating.json', 'w') as f:
        json.dump(rating, f, ensure_ascii=False, indent=4)

player_name = os.environ.get('USER')
print(f'Hello {player_name}!')
while True:
    select_level(player_name)

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
