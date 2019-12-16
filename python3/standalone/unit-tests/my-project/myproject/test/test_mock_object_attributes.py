from unittest.mock import Mock

from myproject.main import function_d


def test_function_d():
    mock_obj = Mock()
    mock_obj.name = "foo"

    assert function_d(mock_obj) == "FOO"
