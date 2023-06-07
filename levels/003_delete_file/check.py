import os
usr=os.environ.get("USER")

if 'delete_me.txt' not in os.listdir(f'/home/{usr}'):
    print(1)
else:
    print(0)