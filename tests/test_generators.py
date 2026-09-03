import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(test_transactions, test_transactions_1):
    assert next(filter_by_currency(test_transactions, "USD")) == test_transactions_1
    assert next(filter_by_currency([], "USD")) == {}
    with pytest.raises(StopIteration):
        next(filter_by_currency(test_transactions, "RUB"))


def test_transaction_descriptions(test_transactions):
    assert next(transaction_descriptions(test_transactions)) == "Перевод организации"
    assert next(transaction_descriptions([])) == "Список пуст"


@pytest.mark.parametrize("start, stop, result", [(1, 5, "0000 0000 0000 0001"), ("1", "5", "Не верные данные")])
def test_card_number_generator(start, stop, result):
    assert next(card_number_generator(start, stop)) == result
