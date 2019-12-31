from unittest.mock import mock_open, patch

from myproject.main import file_contents_to_uppercase


def test_file_contents_to_upper_case():
    m = mock_open(read_data="foo bar")

    with patch('myproject.main.open', m):
        assert file_contents_to_uppercase("path/to/file") == "FOO BAR"
