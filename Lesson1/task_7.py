a, b, c = input('Ведите стороны треугольника через пробел ').split(' ')

a = int(a)
b = int(b)
c = int(c)

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Треугольник РАВНОСТОРОННИЙ")
    elif a == b or a == c or b == c:
        print("Треугольник РАВНОБЕДРЕННЫЙ")
    else:
        print("Треугольник РАЗНОСТОРОННИЙ")
else:
    print("ЧТО ТЫ ТАКОЕ?")
