import os
usr = os.environ.get('USER')

if os.path.isdir(f"/home/{usr}/new_directory"):
    print("1")
else:
    print("0")