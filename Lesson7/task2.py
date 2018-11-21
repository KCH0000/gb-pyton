import test_lesson as test


def merge_sort(array):
    len_array = len(array)

    if len_array <= 1:
        return array

    left = merge_sort(array[:len_array//2])
    right = merge_sort(array[len_array//2:len_array])
    i = j = 0
    result = []

    while i < len(left) or j < len(right):
        if i >= len(left):
            result.append(right[j])
            j += 1
        elif j >= len(right):
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    return result


SIZE = 100
array = test.rand_array(0, 50, SIZE)

print(array)
print(merge_sort(array))

test.test_sort(merge_sort, 10000, SIZE, -100, 99, False)
