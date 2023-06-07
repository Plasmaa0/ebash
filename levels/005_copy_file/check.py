import os
from pre import string_to_compare
usr=os.environ.get("USER")

if 'exbash.txt' in os.listdir(f'/home/{usr}/copy_here'):
    with open(f'/home/{usr}/copy_here/exbash.txt', "r") as f:
        if f.read().strip() == string_to_compare.strip():
            print(1)
        else:
            print(0)
else:
    print(0)