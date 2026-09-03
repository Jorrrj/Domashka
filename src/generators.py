def filter_by_currency(list_of_dicts, currency):
    """Функция, которая принимает на вход список словарей,
    представляющих транзакции. Функция должна возвращать итератор,
     который поочередно выдает транзакции,
      где валюта операции соответствует заданной."""
    if len(list_of_dicts) != 0:
        for i in list_of_dicts:
            if i.get("operationAmount").get("currency").get("name") == currency:
                yield i
    else:
        yield {}


def transaction_descriptions(list_of_dicts):
    """Функция, которая принимает на вход список словарей,
    представляющих транзакции.
    Функция должна возвращать описание каждой транзакции."""

    if len(list_of_dicts) != 0:
        for i in list_of_dicts:
            yield i.get("description")
    else:
        yield "Список пуст"


def card_number_generator(start, stop):
    """Генератор должен принимать начальное и конечное значения для генерации диапазона номеров карт"""
    if isinstance(start, int) is True and isinstance(stop, int) is True:
        for number in range(start, stop + 1):
            num_card = str(number).zfill(16)  # Функция которая добавлят нули слева
            yield num_card[0:4] + " " + num_card[4:8] + " " + num_card[8:12] + " " + num_card[12:]
    else:
        yield "Не верные данные"
