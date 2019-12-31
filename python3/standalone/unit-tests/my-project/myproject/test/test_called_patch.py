from unittest.mock import patch

from myproject.main import function_a


def test_called_patch():
    with patch("myproject.main.complex_function", return_value="foo") as patched_function:
        function_a()

    patched_function.assert_called()
