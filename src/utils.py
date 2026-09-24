import json


def read_operations(path_file: str) -> list:
    """Получаем список операций из файла"""
    try:
        with open(path_file, "r", encoding="UTF-8") as file:
            list_operations = json.load(file)
    except FileNotFoundError as e:
        print(f"Ошибка: {e}")
        list_operations = []
    if isinstance(list_operations, list) is False:
        list_operations = []
    elif list_operations == []:
        print("Список операций пуст")
    return list_operations
