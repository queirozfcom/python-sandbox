from unittest.mock import Mock


def my_function(some_object):
    output = some_object.foo().bar.baz().quux()

    return output.upper()


def test_chained():
    mock_obj = Mock()

    result_1 = mock_obj.foo.return_value
    result_2 = result_1.bar.baz.return_value
    result_2.quux.return_value = "hello world"

    assert my_function(mock_obj) == "HELLO WORLD"
