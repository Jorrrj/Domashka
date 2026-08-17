from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_number_card: str) -> str:
    """Создаем функцию которая умеет обрабатывать информацию как о картах, так и о счетах"""

    if len(account_number_card) == 0:
        return "Ошибка данных"
    if "Счет" in account_number_card:

        mask_account = get_mask_account(account_number_card[5:])
        return f"Счет {mask_account}"
    else:
        number_card = account_number_card.split(" ")
        # Разделение строки на элементы списка по пробелу
        number_card[-1] = get_mask_card_number(number_card[-1])
        # Сначала маскировка последнего элемента списка
        # (с помощью функции импортирования из модуля mask.py)
        # перезапись последнего элемента списка

        return " ".join(number_card)  # Объединили элементы списка в строку


def get_date(date: str) -> str:
    """Преобразование формата даты"""
    # date_new = date[0:10].split("-")
    # return f"{date_new[2]}.{date_new[1]}.{date_new[0]}"
    dt = datetime.fromisoformat(date)
    return dt.strftime("%d.%m.%Y")
