from os import mkdir, listdir
import argparse

def create_level(name, folder, description, hint, readme,about):
    level_num = len(listdir('levels'))
    new_level_num = str(level_num).rjust(3,'0')
    folder_name = 'levels/' + new_level_num+'_'+folder.lower().replace(' ', '_')
    mkdir(folder_name)
    with open(f"{folder_name}/HINT.txt", 'w') as hint_file:
        hint_file.write(hint)
    with open(f"{folder_name}/README.txt", 'w') as readme_file:
        readme_file.write('You can write markdown here\n'+readme)
    with open(f"{folder_name}/ABOUT.txt", 'w') as about_file:
        about_file.write(about)
    with open(f"{folder_name}/check.py", 'w') as script_file:
        script_file.write('# write your checking code here. it must output 0 or 1 as False/True as result of check.\nprint(1)\n')
    with open(f"{folder_name}/pre.py", 'w') as script_file:
        script_file.write('# this code will be executed BEFORE level starts\n# do what you want here to prepare computer for level\n# USER WON\'T SEE ANY OUTPUT FROM THIS FILE')
    with open(f"{folder_name}/post.py", 'w') as script_file:
        script_file.write('# this code will be executed AFTER level starts\n# do what you want here to clean up after level\n# USER WON\'T SEE ANY OUTPUT FROM THIS FILE')

parser = argparse.ArgumentParser(description='Create template folder for new level.')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-n', '--new', dest='name', type=str, nargs=1, help="Generate template level folder.")
args = parser.parse_args()

if args.name is not None:
    name = args.name[0]
    print(f"Generating template for level with name '{name}'.")
    try:
        create_level(name, name, f"Sample decription for level {name}\n", f"Sample hint for level {name}\n", f"Sample readme for level {name}\n", f"Sample about for level {name}\n")
    except Exception as e:
        print(f"Failed with exception: {e}")
else:
    print('Give me name of new level!!!')
