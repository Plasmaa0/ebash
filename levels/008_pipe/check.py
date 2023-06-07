# write your checking code here. it must output 0 or 1 as False/True as result of check.

import os
usr = os.environ.get("USER")

apples_file = f'/home/{usr}/apples.txt'
# проверяем, что файл apples.txt был создан и содержит правильный результат
if os.path.exists(apples_file):
    with open(apples_file, 'r') as f:
        content = f.read()
        if 'red apple\ngreen apple\n' == content:
            print(1)
        else:
            print(0)
else:
    print(0)