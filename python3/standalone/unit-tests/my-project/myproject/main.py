from myproject.helpers import complex_function, complex_function_with_params


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


def function_e(param1, param2):
    return complex_function_with_params(param1.upper(), param2.upper())


def file_contents_to_uppercase(path_to_file):
    with open(path_to_file, "r") as f:
        contents = f.read()

        return contents.upper()
