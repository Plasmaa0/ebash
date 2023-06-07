# this code will be executed AFTER level starts
# do what you want here to clean up after level
# USER WON'T SEE ANY OUTPUT FROM THIS FILE

import shutil, os
usr = os.environ.get('USER')

dir = f"/home/{usr}/new_directory"
if os.path.isdir(dir):
    shutil.rmtree(dir)