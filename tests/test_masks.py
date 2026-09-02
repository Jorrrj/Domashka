import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number_str, result",
    [("1111111111111111", "1111 11** **** 1111"), ("11111111111111111", "Ошибка данных")],
)
def test_get_mask_card_number(number_str, result):
    assert get_mask_card_number(number_str) == result


@pytest.mark.parametrize(
    "number_str, result",
    [("11111111111111111111", "**1111"), ("11111111111111111", "Ошибка данных")],
)
def test_get_mask_account(number_str, result):
    assert get_mask_account(number_str) == result
