from myproject.helpers import complex_function


class MyClass:
    def __init__(self, name):
        self.name = name

    def sayhi(self):
        return "hi my name is: {}".format(self.name)


def function_a():
    return complex_function().upper()


def function_b():
    param1 = MyClass("foo")

    return param1.sayhi()


if __name__ == '__main__':
    obj = MyClass("foo")

    function_b(obj)
