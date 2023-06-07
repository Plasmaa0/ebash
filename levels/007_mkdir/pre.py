# this code will be executed BEFORE level starts
# do what you want here to prepare computer for level
# USER WON'T SEE ANY OUTPUT FROM THIS FILE

import shutil, os
usr = os.environ.get('USER')

dir = f"/home/{usr}/new_directory"
if os.path.isdir(dir):
    shutil.rmtree(dir)