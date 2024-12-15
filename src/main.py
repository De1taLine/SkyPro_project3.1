import math


def add_numbers(a, b):
    return a + b


def is_even(a):
    return a % 2 == 0


def find_max(my_list):
    if len(my_list) > 0:
        return max(my_list)
    return 0


def divide(a, b):
    if b > 0:
        return a / b
    return 0


def calculate_logarithm(x, base):
    return math.log(x, base)


def reverse_string(my_string):
    return my_string[::-1]


def finder(my_list, my_type):
    counter = 0
    if isinstance(my_list, list):
        for item in my_list:
            if isinstance(item, my_type):
                counter += 1
    return counter


if __name__ == '__main__':
    assert add_numbers(2, 2) == 4

    assert is_even(2) == True

    assert find_max([1, 2, 3, 4, 5]) == 5
