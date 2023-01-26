# 1) Create a decorator that will count how many times
# # the decorated function was called.

def m_counter(func):
    """
    A decorator that count how many times
    the decorated function was called.
    :param func: decorated function
    :return: function
    """

    def inner(*args, **kwargs):
        inner.count += 1
        return func(*args, **kwargs)
    inner.count = 0
    return inner


@m_counter
def func_x():
    return "Hello"


@m_counter
def func_y(name):
    return f"Hello, {name}"


print(func_x())
print(func_x())
print(func_x())
print(func_y("Petro"))
print(func_y("Hanna"))
print(func_x.count)
print(func_y.count)


# 2) Create a decorator that will register decorated function in the list of functions
# to process the sequence.

x = []


def decorator(func):
    """
    This decorator registers decorated function in the list of functions.
    :param func: decorated function
    :return: decorated function
    """
    x.append(func)
    return func


@decorator
def func_1():
    return f"Hello1"


@decorator
def func_2():
    return "Hello2"


@decorator
def func_3():
    return "Hello3"


print(func_1())
print(func_2())
print(func_3())
print(x)


# 3) A class has a __str__ method that returns string based on class.
# Create a decorator for this method, so that the resulting string
# is saved to a text file whose name matches the name
# of the class whose method you decorated.

def decorator_str_to_file(func):
    def inner(*args, **kwargs):
        name = f"{func.__qualname__.split('.')[0]}.txt"
        res = func(*args, **kwargs)
        with open(name, "a") as f:
            f.write(f"{res}\n")
        return res
    return inner


class Student:

    def __init__(self, surname: str, name: str):
        self.surname = surname
        self.name = name

    @decorator_str_to_file
    def __str__(self):
        return f"{self.name} {self.surname}"


st = Student("Rii", "Andrii")
print(st)


# 4) Create a decorator with parameters to time the job of function.
# The parameters should be how many times you need run the decorated function
# and in which file to save the results timing.
# The goal is to time the decorated function.

import time


def time_measure(number: int, file_name: str):
    """
    The decorator function that measures during of function work.
    :param number: the number of function calls
    :param file_name: name of the file with measurement results.
    :return: function.
    """
    def decorator_str_to_file(func):
        def inner(*args, **kwargs):
            start = time.time()
            for _ in range(number):
                res = func(*args, **kwargs)
            stop = time.time()

            with open(file_name, "a") as f:
                f.write(f"{stop-start}\n")
            return res
        return inner
    return decorator_str_to_file


class Student:

    def __init__(self, surname: str, name: str):
        self.surname = surname
        self.name = name

    @time_measure(1_000_000, "timing_func.txt")
    def __str__(self):
        return f"{self.name} {self.surname}"


st = Student("Rii", "Andrii")
print(st)

# 1) Create a decorator that registers the decorated class in a list of classes.

cls_list = []


def decorator_cls(cls):
    """
    The decorator that registers the decorated class in a list of classes.
    :param cls: decorated class
    :return: cls
    """
    cls_list.append(cls)
    return cls


@decorator_cls
class X:
    def __init__(self):
        pass


@decorator_cls
class B:
    def __init__(self):
        pass


x = X()
b = B()
print(cls_list)


# 2) Create a class decorator with a parameter. The parameter must be
# the string that should be appended (on the left) to the result of the __str__ method.

class DecorAddStr:
    def __init__(self, add_str: str):
        self.add_str = add_str

    def __call__(self, cls):
        text_from_cls_str = cls.__str__

        def __str__(self):
            return f"{self.add_str}{text_from_cls_str(self)}"

        cls.add_str = self.add_str
        cls.__str__ = __str__

        return cls


@DecorAddStr("Hello ")
class P:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name}"


person_1 = P("Hanna")
print(person_1)


# 3) Write a static method for the Box class that will calculate common volume of two boxes,
# which will be parameters.

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"{self.x}*{self.y}*{self.z}"

    @staticmethod
    def calc_volume(instance_1, instance_2):
        res = (instance_1.x * instance_1.y * instance_1.z) + (instance_2.x * instance_2.y * instance_2.z)
        return res


box_1 = Box(1, 2, 3)
box_2 = Box(5, 5, 5)
print(Box.calc_volume(box_1, box_2))

#