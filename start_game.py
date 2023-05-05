import json
import sys

inp = sys.stdin.readline().strip()
uuid = inp.split('|')[0].strip()

with open('levels.json', 'r') as f:
    levels = json.load(f)
    level = [i for i in levels if i['uuid'] == uuid][0]
    print(level['folder'])
