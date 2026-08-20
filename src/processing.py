def filter_by_state(user_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция которая принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED').
     Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""

    new_list = []
    # Переменная куда будут попадать отсортированные
    # данные по ключу state со значением по умолчанию EXECUTED

    if len(user_list) != 0:
        for item in user_list:
            if item.get("state") == state:
                new_list.append(item)
        # Перебор списка словарей
        # Поиск в словаре ключа state и сравнение его значения переменной state
        # По умолчанию = EXECUTED при совпадении добавляется в new_list

    return new_list


def sort_by_date(user_list: list[dict], sorter: bool = True) -> list[dict]:
    """Функция которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)."""

    new_list = sorted(user_list, key=lambda k: k["date"], reverse=sorter)
    # Сортировка списка словарей по по ключу date словарей (через lambda функцию где к - это словарь)

    return new_list



