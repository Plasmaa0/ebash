# write your checking code here. it must output 0 or 1 as False/True as result of check.

import os
usr=os.environ.get("USER")

if 'file.txt' in os.listdir(f'/home/{usr}'):
    print(1)
else:
    print(0)