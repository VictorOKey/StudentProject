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


from json_db_lite import JSONDatabase

_db = JSONDatabase(file_path='students.json')

def json_to_dict_list():
    return _db.get_all_records()

def add_student(student: dict):
    student['date_of_birth'] = student['date_of_birth'].strftime('%Y-%m-%d')
    _db.add_records(student)
    return True

def update_student(update_filter: dict, new_data: dict):
    _db.update_record_by_key(update_filter,new_data)
    return True

def delete_student(key: str, value: str):
    _db.delete_record_by_key(key, value)
    return True