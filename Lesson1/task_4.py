import random

a, b = input("Введите два числа через пробел:").split(" ")

a = int(a)
b = int(b)

if a < b:
    minN = a
    maxN = b
else:
    minN = b
    maxN = a
print(f'Случайное не случанойно {random.randint(minN, maxN)}')

a, b = input("Введите два числа через пробел:").split(" ")

a = float(a)
b = float(b)

if a < b:
    minN = a
    maxN = b
else:
    minN = b
    maxN = a
print(f'Случайное не случанойно {random.uniform(minN, maxN)}')

c, d = input("Введите две буквы через пробел:").split(" ")
a = ord(c.upper())
b = ord(d.upper())

if a < b:
    minN = a
    maxN = b
else:
    minN = b
    maxN = a
r = random.randint(minN, maxN)

print(f'Случайная буква {chr(r)}')