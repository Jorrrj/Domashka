import json
import os
from unittest.mock import Mock

from src.utils import read_operations


def test_read_operations(test_transactions):
    mock_json = Mock(return_value=test_transactions)
    json.load = mock_json
    assert (
        read_operations(os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")) == test_transactions
    )


def test_read_operations_1():
    mock_json = Mock(return_value=[])
    json.load = mock_json
    assert read_operations(os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")) == []


def test_read_operations_2():
    mock_json = Mock(return_value=[])
    json.load = mock_json
    assert read_operations(os.path.join(os.path.dirname(__file__), "..", "dat", "operations.json")) == []


def test_read_operations_3():
    mock_json = Mock(return_value="")
    json.load = mock_json
    assert read_operations(os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")) == []
