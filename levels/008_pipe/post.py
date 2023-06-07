# this code will be executed AFTER level starts
# do what you want here to clean up after level
# USER WON'T SEE ANY OUTPUT FROM THIS FILE

import os
usr = os.environ.get("USER")

# удаляем созданный файл fruits.txt
if os.path.exists(f'/home/{usr}/apples.txt'):
    os.remove(f'/home/{usr}/apples.txt')