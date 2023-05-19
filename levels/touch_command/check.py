import os
from pathlib import Path

if 'i_am_learning_touch_command.txt' in os.listdir(Path.home()):
    print(1)
else:
    print(0)
