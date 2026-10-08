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
    result_list = []
    for i in list_operations:
        res_dict = {}
        res_dict["id"] = i.get("id")
        res_dict["state"] = i.get("state")
        res_dict["date"] = i.get("date")
        res_dict["amount"] = i.get("operationAmount", {}).get("amount")
        res_dict["currency_name"] = i.get("operationAmount", {}).get("currency", {}).get("name")
        res_dict["currency_code"] = i.get("operationAmount", {}).get("currency", {}).get("code")
        res_dict["from"] = i.get("from")
        res_dict["to"] = i.get("to")
        res_dict["description"] = i.get("description")
        result_list.append(res_dict)
    return result_list
