import csv

import pandas as pd


def read_csv(path_file: str) -> list:
    """Функция считывания данных с csv файла"""
    list_transaction = []
    try:
        with open(path_file, encoding="UTF-8") as f:
            data = csv.DictReader(f, delimiter=";")
            for transaction in data:
                list_transaction.append(transaction)
    except FileNotFoundError as e:
        print(e)
    return list_transaction


def read_xlsx(path_file: str) -> list:
    """Функция считывания данных с xlsx файла"""
    try:
        data = pd.read_excel(path_file)
        new_data = data.fillna(0)
        list_transaction = new_data.to_dict(orient="records")
    except FileNotFoundError as e:
        print(e)
        list_transaction = []
    except Exception as ex:
        print(f"Возникла ошибка: {ex}")
        list_transaction = []
    return list_transaction
