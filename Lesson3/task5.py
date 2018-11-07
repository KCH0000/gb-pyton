import random

SIZE = 10
array = [random.randint(-SIZE * SIZE // 2, SIZE * SIZE // 2) for _ in range(SIZE)]
print(array)

negative_max_p = 0
while 0 <= array[negative_max_p]:
    negative_max_p += 1

for i in range(negative_max_p + 1, len(array)):
    if 0 > array[i] > array[negative_max_p]:
        negative_max_p = i

print(f'Максимальное отрицательное {array[negative_max_p]}, на позиции {negative_max_p}')
