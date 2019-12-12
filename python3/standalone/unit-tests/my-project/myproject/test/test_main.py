from unittest.mock import patch

from myproject.main import function_a


def test_function_a():
    with patch("myproject.main.complex_function") as complex_function_mock:
        complex_function_mock.return_value = "foo"

        assert function_a() == "FOO"
