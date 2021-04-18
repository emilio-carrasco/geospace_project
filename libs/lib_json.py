import json
from bson.json_util import dumps 


def save_json(l,path,nombre):
    json_data = dumps(l, indent = 2)

    with open(f'{path}/{nombre.strip()}.json', 'w') as file:
        file.write(json_data)

def open_json(path):
    with open(path) as f:
        data = json.load(f)
    return data