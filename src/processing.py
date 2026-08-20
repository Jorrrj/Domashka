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


if __name__ == "__main__":
    h = [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(sort_by_date(h, False))
    print(filter_by_state(h, "CANCELED"))
