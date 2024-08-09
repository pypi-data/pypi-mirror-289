import json

def txt_read(path):
    with open(path) as f:
        content = f.read()
    return content

def json_read(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
