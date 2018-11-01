def counter(num):
    global odd, even
    if 0 == num:
        return
    else:
        if a % 2 == 0:
            odd = odd + 1
        else:
            even = even + 1
    counter(num // 10)


odd = 0
even = 0
a = int(input('Введите натуральное число: '))
counter(a)
print(f'Вчисл {a} {odd} четных цифр и {even} нечетных')
