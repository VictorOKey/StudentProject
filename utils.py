import json

def list_to_json(list, filename):
    try:
        json_str = json.dumps(list, ensure_ascii=False)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(json_str)
        return json_str
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при преобразование списка в JSON: {e}")
        return None

def json_to_list(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            json_str = file.read()
            list = json.loads(json_str)
        return list
    except (TypeError, ValueError, IOError) as e:
        print(f"Ошибка при чтении JSON из файла: {e}")
        return None