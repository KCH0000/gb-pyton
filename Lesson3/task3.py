import random

SIZE = 10
array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]

max_position = min_position = 0

for i in range(1, len(array)):
    if array[i] > array[max_position]:
        max_position = i
    if array[i] < array[min_position]:
        min_position = i

print('В Массиве')
print(array)
print(f'Минимальный элемент = {array[min_position]}')
print(f'Максимальный элемент = {array[max_position]}')

array[max_position], array[min_position] = array[min_position], array[max_position]

print('После переустановки выглидит')
print(array)
