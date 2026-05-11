
from math import *

def calculate(a, b):
    result = a + b
    return result


def bad_function():
    x = 10
    y = 20
    z = x + y
    return z


def unused_function():
    pass


def division(a, b):
    return a / b  # no zero division check (intentional issue)


print(calculate(5, 10))
print(bad_function())
