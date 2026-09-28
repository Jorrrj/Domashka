import json
import logging

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler_utils = logging.FileHandler("logs/utils.log", mode="w", encoding="UTF-8")
file_formatter_utils = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler_utils.setFormatter(file_formatter_utils)
logger.addHandler(file_handler_utils)


def read_operations(path_file: str) -> list:
    """Получаем список операций из файла"""
    try:
        with open(path_file, "r", encoding="UTF-8") as file:
            list_operations = json.load(file)
            logger.info("Данные считаны с файла")
    except FileNotFoundError as e:
        logger.error("Файл не найден")
        print(f"Ошибка: {e}")
        list_operations = []
    if isinstance(list_operations, list) is False:
        list_operations = []
        logger.info("В файле нет списка")
    elif list_operations == []:
        print("Список операций пуст")
    return list_operations
