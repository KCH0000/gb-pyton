def mirorer(num):
    global res
    if 0 == num:
        return
    else:
        res = res * 10 + num % 10
    mirorer(num // 10)


res = 0

a = int(input('Введите натуральное число: '))
mirorer(a)
print(f'Отраженное число {a} равно {res}')
