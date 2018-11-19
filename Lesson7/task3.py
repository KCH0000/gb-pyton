import test_lesson as test
import collections as c


def median_array(array):
    if len(array) % 2 == 0:
        return False
    array = c.deque(array)

    for i in range(len(array) // 2 + 1):
        min = 0
        for i in range(len(array)):
            if array[i] < array[min]:
                min = i
            else:
                i += 1
        array[0], array[min] = array[min], array[0]
        result = array.popleft()
    return result


SIZE = 5
array = test.rand_array(-100, 200, 2 * SIZE + 1)

print(array)
print(median_array(array))


test.test_median(median_array, 100000, 2 * SIZE + 1, -100, 200,)
