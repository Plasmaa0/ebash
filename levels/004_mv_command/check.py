# write your checking code here. it must output 0 or 1 as False/True as result of check.
import os
usr = os.environ.get('USER')

def file_in_dir(file, dir):
    return file in os.listdir(dir)

def move_task():
    return file_in_dir('move_me.txt', f'/home/{usr}/end') and not file_in_dir('move_me.txt', f'/home/{usr}/start')

def rename_task():
    return file_in_dir('new_name.txt', f'/home/{usr}') and not file_in_dir('rename_me.txt', f'/home/{usr}')

def check():
    if not (move_task()):
        return False
    if not (rename_task()):
        return False
    return True

if __name__ == "__main__":
    print(int(check()))