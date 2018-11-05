import random

SIZE = 10
array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
print(array)

max_position = min_position = 0

for i in range(1, len(array)):
    if array[i] > array[max_position]:
        max_position = i
    if array[i] < array[min_position]:
        min_position = i

if min_position > max_position:
    min_position, max_position = max_position, min_position

summ = 0
print('Cумма:')
for i in range(min_position + 1, max_position):
    print(array[i])
    summ += array[i]

print(f'равна {summ}')
