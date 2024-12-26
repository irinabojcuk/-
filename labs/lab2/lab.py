from random import randint
from module import *


def result():
    array = [randint(-10, 10) for _ in range(50)]

    print('ARRAY: ')
    print(array)
    print('-'*20)

    print('QUICKSORT FUNC: ')
    print(quicksort(array))
    print('-'*20)

    print('FIND_ELEMENT FUNC: ')
    print(find_element(array, array[randint(0, len(array)-1)]))
    print('-' * 20)

    print('FIND_SEQUENCE FUNC: ')
    print(find_sequence(array))
    print('-' * 20)

    print('MIN5 FUNC: ')
    print(min5(array))
    print('-' * 20)

    print('MAX5 FUNC: ')
    print(max5(array))
    print('-' * 20)

    print('AVERAGE FUNC: ')
    print(average(array))
    print('-' * 20)

    print('NO_DUPLICATES FUNC: ')
    print(no_double(array))
    print('-' * 20)

    print('RAN SUCCESSFULLY')


result()
