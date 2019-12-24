from unittest.mock import Mock


def function_e(some_obj, argument):
    return some_obj.some_method(argument)

def test_arguments():
    mock = Mock()
    mock.some_method = Mock(return_value=None)

    function_e(mock, "foo bar")

    mock.some_method.assert_called()

    # arguments passed to method some_method
    arguments_tuple = mock.some_method.call_args[0]

    assert "foo bar" in arguments_tuple
