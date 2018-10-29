number = input("Введите число ")
if 100 <= int(number) < 1000:
    a, b, c = number
    a = int(a)
    b = int(b)
    c = int(c)
    print("Сумма цифр равна ", a + b + c)
    print("Произведение цифр равно ", a * b * c)
else:
    print("Неверный ввод")
