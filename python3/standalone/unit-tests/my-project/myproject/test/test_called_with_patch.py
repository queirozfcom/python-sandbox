from unittest.mock import patch

from myproject.main import function_e


def test_called_with_patch():
    with patch("myproject.main.complex_function_with_params", return_value=None) as patched_function:
        # function_e converts the params to upper case and
        # calls another function with those
        function_e("foo", "bar")

    patched_function.assert_called_with("FOO", "BAR")
