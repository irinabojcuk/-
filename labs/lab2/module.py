def quicksort(array):
    """
    :param array: list of numbers
    :return: sorted array
    Time complexity:
                    Worst case: O(n^2)
                    Best case: O(n*log(n))
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


def find_element(array, x):
    """
    :param array: list of numbers
    :param x: element from the list
    :return: index of x

    Time complexity: O(n)
    """
    return array.index(x)


def find_sequence(lst):
    """

    :param lst: list of numbers
    :return: sequence of elements if any found
    Time Complexity: O(n)
    """
    my_sequences = []
    for idx, item in enumerate(lst):
        if not idx or item - 1 != my_sequences[-1][-1]:
            my_sequences.append([item])
        else:
            my_sequences[-1].append(item)
    return max(my_sequences, key=len)


def min5(array):
    """
    :param array: list of numbers
    :return: first 5 smallest elements
    Time Complexity: O(n*log2*n)
    """
    return sorted(array)[:5]


def max5(array):
    """
    :param array: list of numbers
    :return: first 5 greatest elements
    Time Complexity: O(n*log2*n)
    """
    return sorted(array, reverse=True)[:5]


def average(array):
    """
    :param array: list of numbers
    :return: average of elements
    Time Complexity: O(n)
    """
    return sum(array)/len(array)


def no_double(array):
    """
    :param array: list of numbers
    :return: array with no duplicates
    Time Complexity: O(n)
    """
    return list(set(array))


