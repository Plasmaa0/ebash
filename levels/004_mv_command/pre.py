# this code will be executed BEFORE level starts
# do what you want here to prepare computer for level
# USER WON'T SEE ANY OUTPUT FROM THIS FILE
import os
usr = os.environ.get('USER')
os.mkdir(f'/home/{usr}/start')
os.mkdir(f'/home/{usr}/end')
os.system(f'touch /home/{usr}/start/move_me.txt')
os.system(f'touch /home/{usr}/rename_me.txt')
os.mkdir(f'/home/{usr}/end')