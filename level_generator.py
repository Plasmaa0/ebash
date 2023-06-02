import json
import random
import uuid
from os import mkdir, system
from string import ascii_lowercase
import argparse


def generate_random_levels(amount: int = 15) -> None:
    levels = []
    rstr = lambda length: ''.join(random.sample(ascii_lowercase * 100, length))
    for _ in range(amount):
        levels.append(create_level(rstr(10), rstr(10), rstr(100), rstr(50), rstr(500),rstr(30)))
    with open('levels.json', 'w') as f:
        json.dump(levels, f, indent=4)


def create_level(name, folder, description, hint, readme,about):
    folder_name = 'levels/level_' + folder.lower().replace(' ', '_')
    level = {
        "completed": False,
        "name": name,
        "description": description,
        "folder": folder_name,
        "uuid": str(uuid.uuid4())
    }
    mkdir(folder_name)
    with open(f"{folder_name}/HINT.txt", 'w') as hint_file:
        hint_file.write(hint)
    with open(f"{folder_name}/README.txt", 'w') as readme_file:
        readme_file.write(readme)
    with open(f"{folder_name}/ABOUT.txt", 'w') as about_file:
        about_file.write(about)
    with open(f"{folder_name}/check.sh", 'w') as script_file:
        script_file.write('# write your checking code here. it must output 0 or 1 as False/True as result of check.\necho 1')
    return level


parser = argparse.ArgumentParser(description='Generate random levels. Or created template folder for new level.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-r', '--random', dest='N', type=int, nargs=1, help="Generate random levels")
group.add_argument('--clear', action='store_true', help="Delete all levels")
group.add_argument('-n', '--new', dest='name', type=str, nargs=1,
                   help="Generate template level folder and add it to .json database")
args = parser.parse_args()

if args.name is not None:
    name = args.name[0]
    print(f"Generating template for level with name '{name}'.")
    try:
        level = create_level(name, name, f"Sample decription for level {name}", f"Sample hint for level {name}\n", f"Sample readme for level {name}\n", f"Sample about for level {name}\n")
        try:
            with open('levels.json', 'r') as f:
                levels = json.load(f)
        except:
            levels = []
        with open('levels.json', 'w') as f:
            levels.append(level)
            json.dump(levels, f, indent=4)
    except Exception as e:
        print(f"Failed with exception: {e}")
if args.N is not None:
    n = args.N[0]
    print(f"Generating {n} random levels")
    generate_random_levels(n)
if args.clear is not None:
    if args.clear:
        print("This action will delete everything inside levels folder. Are you sure? [y/N]: ", end='')
        choice = input()
        if choice in ['y', 'Y']:
            print("Clearing levels folder")
            system("rm levels/* -rfd")
            system("rm levels.json")
            print(f"Done")
        else:
            print("Nothing done")
