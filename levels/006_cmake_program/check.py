import os
import subprocess
import time 

def check():
    try:
        usr=os.environ.get("USER")
        os.chdir(f'/home/{usr}/cmake_program/build')
        try:
            generate_output=subprocess.check_output(['cmake', '..'])
            build_output=subprocess.check_output(['cmake','--build','.'])
        except:
            print(0)
            return
        success = subprocess.check_output('./my_program').strip()==b"Hello, World!"
        print(int(success))
    except:
        print(0)

if __name__ == "__main__":
    check()