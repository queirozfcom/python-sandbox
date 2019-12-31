from unittest.mock import Mock


def function_with_call(some_obj, argument):
    return some_obj.some_method(argument)


def function_without_call(some_obj):
    output = str(some_obj)

    return output


def test_called():
    mock = Mock()
    mock.some_method = Mock(return_value=None)

    function_with_call(mock, "foo bar")

    # will return true if method was called one or more times
    mock.some_method.assert_called()


def test_not_called():
    mock = Mock()
    mock.some_method = Mock(return_value="foo")

    function_without_call(mock)

    mock.assert_not_called()
