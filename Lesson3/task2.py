import random

SIZE = 10
array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
res = []

for i in range(0, len(array)):
    if array[i] % 2 == 0:
        res.append(i + 1)
print('Номера четных чисел в массиве')
print(array)
print('равны')
print(res)
