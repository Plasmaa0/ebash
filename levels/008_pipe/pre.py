# this code will be executed BEFORE level starts
# do what you want here to prepare computer for level
# USER WON'T SEE ANY OUTPUT FROM THIS FILE
import os
usr = os.environ.get("USER")

# создаем файл с содержимым для чтения
filename = 'fruits.txt'
with open(f'/home/{usr}/{filename}', 'w') as f:
    f.write('red apple\nyellow banana\norange orange\ngreen apple\npink peach')

# чистим файл apples.txt
if os.path.exists(f'/home/{usr}/apples.txt'):
    os.remove(f'/home/{usr}/apples.txt')