from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(test_user_list, test_result_1, test_result_2):
    assert filter_by_state(test_user_list) == test_result_1
    assert filter_by_state(test_user_list, "CANCELED") == test_result_2
    assert filter_by_state(test_user_list, "CANCELE") == []


def test_sort_by_date(test_user_list, test_result_2_sort, test_result_1_sort):
    assert sort_by_date(test_user_list) == test_result_1_sort
    assert sort_by_date(test_user_list, False) == test_result_2_sort
