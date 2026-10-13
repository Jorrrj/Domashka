from src.processing import filter_by_state, process_bank_operations, process_bank_search, sort_by_date


def test_filter_by_state(test_user_list, test_result_1, test_result_2):
    assert filter_by_state(test_user_list) == test_result_1
    assert filter_by_state(test_user_list, "CANCELED") == test_result_2
    assert filter_by_state(test_user_list, "CANCELE") == []


def test_sort_by_date(test_user_list, test_result_2_sort, test_result_1_sort):
    assert sort_by_date(test_user_list) == test_result_1_sort
    assert sort_by_date(test_user_list, False) == test_result_2_sort


def test_process_bank_search(test_transactions, test_transactions_search):
    assert process_bank_search(test_transactions, "Счет") == test_transactions_search
    assert process_bank_search(test_transactions, "fkhuj") == []
    assert process_bank_search(test_transactions, "") == []


def test_process_bank_operations(test_transactions):
    assert process_bank_operations(test_transactions, ["Перевод организации", "Перевод со счета на счет"]) == {
        "Перевод организации": 1,
        "Перевод со счета на счет": 1,
    }
