# this code will be executed BEFORE level starts
# do what you want here to prepare computer for level
# USER WON'T SEE ANY OUTPUT FROM THIS FILE
import os
usr=os.environ.get("USER")

f = open(f'/home/{usr}/delete_me.txt', "a")
f.write("DELETE ME PLEASE!")
f.close()