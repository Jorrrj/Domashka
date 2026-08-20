from src.widget import mask_account_card, get_date


def test_mask_account_card():
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("") == "Ошибка данных"

def test_get_date():
    assert get_date('2018-06-30T02:08:58.425572') == "30.06.2018"