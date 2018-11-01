print('Калькулятор Мегалатрон 3000')
next = 1

while next:
    x = int(input('Введите первое число: '))
    y = int(input('Введитие второе число: '))
    action = str(input('Что нужно сделать + - * : ? 0 - Завершить: '))

    if '0' == action:
        next = 0
    elif '+' == action:
        print(f'{x} + {y} = {x + y}')
    elif '-' == action:
        print(f'{x} - {y} = {x - y}')
    elif '*' == action:
        print(f'{x} * {y} = {x * y}')
    elif ':' == action:
        if 0 == y:
            print('Деление на ноль')
        else:
            print(f'{x} : {y} = {x / y}')
    else:
        print('Сам это делай')