import json

def read_file():
    try:
        with open('file_Save.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except:
        return {
            "scorer": 0,
            "skin": "rocket.png"
        }

def write_in_file(data):
    with open('file_save.json', 'w', encoding='utf=8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)