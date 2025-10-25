import json
import os

# PATH = 'data'
def load_data(path):
    if not os.path.exists(f'{path}'):
        with open(f'{path}', 'w') as f:
            f.write('[]')
    with open(f'{path}', 'r') as f:
        data = json.load(f)
    return data

def save_data(path, data):
    with open(f'{path}', 'w') as f:
        json.dump(data, f, indent=4)


