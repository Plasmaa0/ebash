import json

with open('levels.json', 'r') as f:
    levels = json.load(f)
    entries = []
    for index, level in enumerate(levels):
        entry = str(index)+' '
        entry += ('да' if level['completed'] else 'нет') + ' '
        entry += '"'+level['name'] + '" '
        entry += '"'+level['description'] + '" '
        entry += level['uuid']
        entries.append(entry)
    result =  ' '.join(entries)
    print(result)
