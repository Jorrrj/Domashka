import os

import requests
from dotenv import load_dotenv

load_dotenv()


def convertion_currency(operations: dict) -> float:
    """Конвертация суммы операций"""
    if operations.get("operationAmount").get("currency").get("code") != "RUB":
        amount = operations.get("operationAmount").get("amount")
        from_currency = operations.get("operationAmount").get("currency").get("code")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={from_currency}&amount={amount}"

        payload = {}
        headers = {"apikey": os.getenv("API_KEY")}

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json().get("result")
    else:
        result = float(operations.get("operationAmount").get("amount"))
    return round(result, 2)
