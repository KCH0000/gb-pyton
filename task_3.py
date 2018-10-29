x1, y1 = input('Ведите, через пробел координаты первой точки ').split(' ')
x2, y2 = input('Ведите, через пробел координаты второй точки ').split(' ')

x1 = int(x1)
x2 = int(x2)
y1 = int(y1)
y2 = int(y2)

a = y1 - y2
b = x2 - x1
c = x1 * y2 - x2 * y1

if a != 0 or b != 0:
    if a == 0:
        print(f'Уравнение прямой y = {-1 * c / b}')
    elif b == 0:
        print(f'Уравнение прямой x = {-1 * c / a}')
    else:
        print(f'Уравнение прямой y = {-1 * a / b}x + {-1 * c / b}')
else:
    print("Точки совпадают")
