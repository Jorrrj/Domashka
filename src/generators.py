def filter_by_currency(list_of_dicts, currency):
    ''' Функция, которая принимает на вход список словарей,
     представляющих транзакции. Функция должна возвращать итератор,
      который поочередно выдает транзакции,
       где валюта операции соответствует заданной. '''
    if len(list_of_dicts) != 0:
        for i in list_of_dicts:
            if i.get("operationAmount").get("currency").get("name") == currency:
                yield i
    else:
        yield {}


def transaction_descriptions(list_of_dicts):
    '''Функция, которая принимает на вход список словарей,
     представляющих транзакции.
     Функция должна возвращать описание каждой транзакции.'''

    if len(list_of_dicts) != 0:
        for i in list_of_dicts:
            yield i.get("description")
    else:
        yield "Список пуст"


def card_number_generator(start, stop):
    ''' Генератор должен принимать начальное и конечное значения для генерации диапазона номеров карт '''
    if isinstance(start, int) is True and isinstance(stop, int) is True:
        for number in range(start, stop + 1):
            num_card = str(number).zfill(16) # Функция которая добавлят нули слева
            yield num_card[0: 4] + " " + num_card[4: 8] + " " + num_card[8: 12] + " " + num_card[12: ]
    else:
        yield "Не верные данные"


if __name__ == '__main__':
    for card_number in card_number_generator(1, 5):
        print(card_number)
    d = [{
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      },
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }]
    usd_transactions = filter_by_currency(d, "USD")
    # for _ in range(2):
    #     print(next(usd_transactions))
    # print(next(usd_transactions))
    # print(next(usd_transactions))

    descriptions = transaction_descriptions(d)
    for _ in range(2):
        print(next(descriptions))
