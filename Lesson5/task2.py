# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
# массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


import collections
from collections.__init__ import deque
from typing import Any


class NumberBase:
    def __init__(self, num_str, base):
        self.base = base
        self.base_dict = []
        for i in range(0, self.base):
            if i < 10:
                self.base_dict.append(chr(48 + i))
            else:
                self.base_dict.append(chr(55 + i))
        self.num = collections.deque(num_str.upper())
        for i in self.num:
            if self.base_dict.count(i) == 0:
                self.base = -1
                print("Введено неверное число")

    def __add__(self, other):
        if self.base != other.base:
            return False  # Тут нужно написать преобразование к общему основанию.
        res: deque[Any] = collections.deque()
        first = other.num
        second = self.num
        first.reverse()
        second.reverse()
        dec = 0
        i = 0
        while i < max(len(first), len(second)) or dec != 0:
            x = self.base_dict.index(second[i]) if i < len(second) else 0
            y = self.base_dict.index(first[i]) if i < len(first) else 0
            res.appendleft(self.base_dict[(x + y + dec) % self.base])
            dec = (x + y + dec) // self.base
            i += 1
        self.sum = ''.join(res)
        return NumberBase(self.sum, self.base)

    def __mul__(self, other):
        if list(self.num) == ['0'] or list(other.num) == ['0']:
            self.num.clear()
            other.num.clear()
            self.num = other.num = ['0']
        if self.base != other.base:
            return False  # Тут нужно написать преобразование к общему основанию.
        first = self.num
        second = other.num
        mult_list = []
        temp = collections.deque()
        dec = 0
        for i in range(0, len(second)):
            temp.clear()
            y = self.base_dict.index(second[i])
            j = i
            while j != 0:
                temp.appendleft('0')
                j -= 1
            j = 0
            while j < len(first) or dec != 0:
                x = self.base_dict.index(first[j]) if j < len(first) else 0
                temp.appendleft(self.base_dict[(x * y + dec) % self.base])
                dec = (x * y + dec) // self.base
                j += 1
            mult_list.append(''.join(temp))
        res = NumberBase('0', self.base)
        for num in mult_list:
            res = res + NumberBase(num, self.base)
        self.mult = ''.join(res.num)
        return res


# base_ = int(input('В какой системе будем считать?(int): '))
# a = input("Ведите первое число: ")
# b = input("Ведите второе число: ")
#
# a = NumberBase(a, base_)
# b = NumberBase(b, base_)

a = NumberBase('556', 16)
b = NumberBase('0', 16)

summ = a + b
mult = a * b

print(f'Сумма = {a.sum}')
print(f'Произведение = {a.mult}')

print(f'Сумма = {summ.num}')
print(f'Произведение = {mult.num}')
