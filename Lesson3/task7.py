import random

SIZE = 10
array = [random.randint(-SIZE * SIZE // 2, SIZE * SIZE // 2) for _ in range(SIZE)]
print(array)

min_p = [0, 0]

for i in range(0, len(array)):
    if array[i] < array[min_p[0]]:
        min_p[0] = i
if min_p[0] == 0:
    st = 1
else:
    st = 0
for i in range(st, len(array)):
    if array[i] < array[min_p[1]] and i != min_p[0]:
        min_p[1] = i

print(array[min_p[0]], array[min_p[1]])
