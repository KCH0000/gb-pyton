n = int(input('Введите натуральное число: '))

curr = 1
res = 0

for i in range(0, n):
    res = res + curr
    curr = -0.5 * curr

print(f'Сумма ряда -1/2n длинной {n} равна {res}')
