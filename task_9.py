a, b, c = input('Ведите 3 числа через пробел ').split(' ')

a = int(a)
b = int(b)
c = int(c)

if b < a < c or c < a < b:
    m = a
elif a < b < c or c < b < a:
    m = b
elif a < c < b or b < c < a:
    m = c
else:
    print("Хмм, мне кажется ты умнее меня")
    exit(0)
print(f'Среди чисел {a} {b} {c} в середние {m}')