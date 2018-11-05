START = 2
STOP = 99
C_START = 2
C_STOP = 9
res = [0] * C_STOP

for i in range(START, STOP + 1):
    for j in range(C_START, C_STOP + 1):
        if i >= j and i % j == 0:
            res[j - 1] += 1
print(f'Количество кратных чисел от {START} до {STOP}')
for i in range(C_START, C_STOP + 1):
    print(f'Для {i} равно {res[i - 1]}')
