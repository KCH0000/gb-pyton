import random

next_step = 1
min_r = 1
max_r = 100
step = 1
a = random.randint(1, 100)

while next_step:
    print(f'Попытка {step}')
    answer = int(input(f'Число а от между {min_r} и {max_r}: '))
    if a == answer:
        print(f'Число {a} было отгадано за {step} шагов')
        next_step = 0
    elif answer > a:
        print(f'а меньше {answer}')
        if answer < max_r:
            max_r = answer
        step = step + 1
    else:
        print(f'а больше {answer}')
        if answer > min_r:
            min_r = answer
        step = step + 1
    if 11 == step:
        print('Фиаско')
        next_step = 0