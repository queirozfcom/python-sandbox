from unittest.mock import Mock

from myproject.main import function_c


def test_function_c():
    mock_obj = Mock()
    mock_obj.sayhi = Mock(return_value="foo")

    # function_c takes as input a MyClass object, calls sayhi() on it
    # and makes the result upper case
    assert function_c(mock_obj) == "FOO"
