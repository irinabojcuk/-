from math import e, sin, cos, sqrt
from sympy import isprime
from random import randint


def result():
    x = float(randint(0, 100))
    print("FUNC1:\n")
    print(func1(x))
    print('-'*20)
    n = int(randint(0, 100))
    print("FUNC2:\n")
    print(func2(n))
    print('-' * 20)
    print("FUNC3:\n")
    print(func3(n))
    print('-' * 20)
    print('RAN SUCCESSFULLY')


def func1(x):
    z = e**x+sin(x)-cos(2*x)
    return f'e^{x}+sin({x})-cos(2*{x})={z}'


def func2(n):

    def divisorGenerator(n):
        large_divisors = []
        for i in range(1, int(sqrt(n) + 1)):
            if n % i == 0:
                yield i
                if i * i != n:
                    large_divisors.append(n / i)
        for divisor in reversed(large_divisors):
            if isprime(int(divisor)):
                yield divisor

    return f"Prime divisors of {n}: {list(divisorGenerator(n))}"


def func3(n):
    array = [randint(-100, 100) for _ in range(n)]
    smallest = min(array)
    negative_sum = sum([i for i in array if i < 0])
    positive = [i for i in array if i > 0]

    return f"array: {array}\nsmallest number: {smallest}\nsum of negative numbers: {negative_sum}\npositive nubmers: {positive}"


result()