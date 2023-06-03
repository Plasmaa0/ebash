import pwd, grp, os, json

ADMIN = os.environ.get('USER')

def create_user(name):
    os.system(f'groupadd ebash_player')
    os.system(f'useradd -m -p $(openssl passwd -1 "1234") {name}')
    os.system(f'usermod -aG ebash_player {name}')
    home_dir = os.path.expanduser(f"~{name}")
    os.system(f"chgrp ebash_player {home_dir}")
    # Change the current working directory to the new user's home directory
    # os.chdir(home_dir)
    
    # Clone the Git repository into the new user's home directory
    os.system(f'su -c "git clone https://github.com/Plasmaa0/ebash {home_dir}/ebash" {name}')
    os.system(f'su -c "pip install -r {home_dir}/ebash/requirements.txt" {name}')
    os.system(f'echo "cd {home_dir}/ebash; python3 ebash.py; exit" >> ~/.bashrc')
    os.system(f'chmod 777 -R {home_dir}')
    os.system(f'passwd -e {name}')

def remove_user(name):
    os.system(f'userdel -r {name}')
    # os.system(f'sudo rm -rf ebash_loser/')

def get_players():
    # Get a dictionary of all user IDs and their corresponding username
    users = {user.pw_uid: user.pw_name for user in pwd.getpwall()}

    players = []
    # Iterate over all user IDs and print their username and group names
    for uid, username in users.items():
        groups = [group.gr_name for group in grp.getgrall() if username in group.gr_mem]
        if 'ebash_player' in groups:
            players.append((username, pwd.getpwuid(uid).pw_dir))
    return players

def read_rating():
    players = get_players()
    global_rating = {}
    for player,homedir in players:
        try:
            with open(f'{homedir}/ebash/rating.json', 'r') as f:
                rating = json.load(f)
                try:
                    global_rating[player] = rating[player]
                except:
                    global_rating[player] = [0,[]]
        except Exception as e:
            print(e)
            continue
    return global_rating

# remove_user("ebash_loser")
# create_user("ebash_loser")

print(read_rating())