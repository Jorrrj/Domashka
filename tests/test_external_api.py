from unittest.mock import patch

from src.external_api import convertion_currency


def test_convertion_currency_1(api_test, test_transactions_1):
    with patch("requests.request") as mock_request:
        mock_request.return_value.json.return_value = api_test
        assert convertion_currency(test_transactions_1) == 698850.23


def test_convertion_currency_2(test_transactions_2):
    assert convertion_currency(test_transactions_2) == 9824.07
