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


def function_c(param):
    output = param.sayhi()

    return output.upper()


def function_d(param):
    name = param.name

    return name.upper()
