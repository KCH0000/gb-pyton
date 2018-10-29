year = int(input('Введите год: '))

if year >= 1582:
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        print('Год Високосный')
    else:
        print('Год обычный')
else:
    print('Трудно сказать')