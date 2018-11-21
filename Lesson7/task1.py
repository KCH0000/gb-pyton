import random
import test_lesson as test

def babble_sort_revers(array):
    n = 0
    while n < len(array):
        for i in range(len(array) - 1 - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


SIZE = 100
array = [random.randint(-100, 99) for _ in range(SIZE)]

print(array)
print(babble_sort_revers(array))

test.test_sort(babble_sort_revers, 1000, SIZE, -100, 99, True)
