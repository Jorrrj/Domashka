import os

from src.generators import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.read_file import read_csv, read_xlsx
from src.utils import read_operations
from src.widget import get_date, mask_account_card


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        ansver_1 = input(
            "Выберите необходимый пункт меню: \n"
            "1. Получить информацию о транзакциях из JSON-файла \n"
            "2. Получить информацию о транзакциях из CSV-файла \n"
            "3. Получить информацию о транзакциях из XLSX-файла \n"
        )
        if ansver_1 == "1":
            print("Для обработки выбран JSON-файл")
            transaction = read_operations(os.path.join(os.path.dirname(__file__), "data", "operations.json"))
            break
        elif ansver_1 == "2":
            print("Для обработки выбран CSV-файл")
            transaction = read_csv(os.path.join(os.path.dirname(__file__), "data", "transactions.csv"))
            break
        elif ansver_1 == "3":
            print("Для обработки выбран XLSX-файл")
            transaction = read_xlsx(os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx"))
            break
        else:
            print("Выбран не верный вариант")

    state = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        ansver_2 = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING \n"
        ).upper()
        if ansver_2 in state:
            transaction = filter_by_state(transaction, ansver_2)
            print(f"Операции отфильтрованы по статусу {ansver_2}")
            break
        else:
            print(f"Статус операции {ansver_2} недоступен.")

    ansver_3 = input("Отсортировать операции по дате? Да/Нет\n").lower()
    if ansver_3 == "да":
        ansver_4 = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        if ansver_4 == "возрастание":
            transaction = sort_by_date(transaction, False)
        elif ansver_4 == "убывание":
            transaction = sort_by_date(transaction)
        else:
            print("Не верно указано направление сортировки")
    ansver_5 = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
    if ansver_5 == "да":
        transaction = list(filter_by_currency(transaction, "RUB"))
    ansver_6 = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
    if ansver_6 == "да":
        ansver_7 = input("Введите слово\n")
        transaction = process_bank_search(transaction, ansver_7)
    print("Распечатываю итоговый список транзакций...")

    num = len(transaction)
    print(f"Всего банковских операций в выборке: {num}")
    for i in transaction:
        date = get_date(i.get("date"))
        desk = i.get("description")
        from_i = mask_account_card(i.get("from"))
        to = mask_account_card(i.get("to"))
        amount = i.get("amount")
        currency_name = i.get("currency_name")
        print(f"{date} {desk}\n {from_i} -> {to}\n Сумма: {amount} {currency_name}\n")


if __name__ == "__main__":
    main()
