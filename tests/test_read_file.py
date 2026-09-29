import csv
import os
from unittest.mock import Mock, patch

from src.read_file import read_csv, read_xlsx


def test_read_csv_error():
    path = os.path.join(os.path.dirname(__file__), "..", "datas", "transactions.csv")
    assert read_csv(path) == []


def test_read_csv(test_transactions):
    path = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
    mock_csv = Mock(return_value=test_transactions)
    csv.DictReader = mock_csv
    assert read_csv(path) == test_transactions
    mock_csv.assert_called_once()


@patch("pandas.read_excel")
def test_read_xlsx(mock_pd, test_transactions):
    mock_pd.return_value.fillna.return_value.to_dict.return_value = test_transactions
    assert read_xlsx("") == test_transactions


def test_read_xlsx_error():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.excel.xlsx")
    assert read_xlsx(path) == []


def test_read_xlsx_error2(capsys):
    read_xlsx({})
    captured = capsys.readouterr()
    assert captured.out == "Возникла ошибка: Invalid file path or buffer object type: <class 'dict'>\n"
