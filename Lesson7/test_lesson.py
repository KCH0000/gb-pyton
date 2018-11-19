import random
import statistics

def rand_array(start, stop, size):
    result = []

    for i in range(size):
        result.append(random.random() * (stop - start) + start)
    return result


def test_sort(func, n, size, stat, stop, revers):
    for i in range(n):
        test_array = rand_array(stat, stop, size)
        if (func(test_array)) != sorted(test_array, reverse=revers):
            print("False")
            return False
    print("Ок")
    return True

def test_median(func, n, size, stat, stop):
    for i in range(n):
        test_array = rand_array(stat, stop, size)
        if (func(test_array)) != statistics.median(test_array):
            print(test_array)
            print(func(test_array))
            print(statistics.median(test_array))
            print("False")
            return False
    print("Ок")
    return True