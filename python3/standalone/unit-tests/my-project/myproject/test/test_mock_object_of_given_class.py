from unittest.mock import patch

from myproject.main import function_b, MyClass

def test_function_b():

    with patch.object(MyClass, 'sayhi', return_value="hi i'm a mock object"):

        # the MyClass object used within function_b will
        # be replaced by a mock defined in the
        # patch.object call above
        assert function_b() == "hi i'm a mock object"
