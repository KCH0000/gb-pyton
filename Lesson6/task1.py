# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Для анализа возьмите любые 1-3 ваших программы. Результаты анализа вставьте в виде комментариев к коду.
# P.S. Напишите в комментариях версию Python и разрядность ОС.
import sys
import random

class MemoryControl:
    def __init__(self):
        self.mem_addrs = {}
        self.mem_sum = 0

    def mem_collect(self, x):
        if id(x)  not in self.mem_addrs:
            self.mem_addrs[id(x)] = sys.getsizeof(x)
        # print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {id(x)}')
        if hasattr(x, '__iter__'):
            if hasattr(x, 'items'):
                for key, value in x.items():
                    self.mem_collect(key)
                    self.mem_collect(value)
            elif not isinstance(x, str):
                for item in x:
                    self.mem_collect(item)
    def mem_total_use(self):
        spam = 0
        for mem in self.mem_addrs:
            spam += self.mem_addrs[mem]
        self.mem_sum = spam
        return self.mem_sum
    def mem_list_clear(self):
        self.mem_addrs.clear()


def func1(test):
    SIZE = 10

    array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
    res = []

    for i in range(0, len(array)):
        test.mem_collect(i)
        if array[i] % 2 == 0:
            res.append(i)
        test.mem_collect(res)
    test.mem_collect(SIZE)
    test.mem_collect(array)


def func2(test):
    for i in range(32, 128, 10):
        line = ''
        for j in range(i, i + 10):
            line = line + f' {j} = {chr(j)}'
            test.mem_collect(i)
            test.mem_collect(j)
            test.mem_collect(line)

def  func3(test):
    SIZE = 10
    test.mem_collect(SIZE)
    array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
    test.mem_collect(array)

    max_position = min_position = 0
    for i in range(1, len(array)):
        if array[i] > array[max_position]:
            max_position = i
        if array[i] < array[min_position]:
            min_position = i
        test.mem_collect(i)
        test.mem_collect(max_position)
        test.mem_collect(min_position)

    if min_position > max_position:
        min_position, max_position = max_position, min_position

    test.mem_collect(max_position)
    test.mem_collect(min_position)
    summ = 0
    for i in range(min_position + 1, max_position):
        summ += array[i]
        test.mem_collect(i)
        test.mem_collect(summ)


test_func = func3

test_obj = MemoryControl()

test_func(test_obj)
print(f'В функции {test_func.__name__} было использовано {test_obj.mem_total_use()} Байт памяти и {len(test_obj.mem_addrs)} адресов')

# print(test_obj.mem_addrs)

# Постарался учесть особенности использования памяти питоном, из-за чего каждый разный запуск используется разное кол-во адресов. По большей части из-за циклов и
# В функции func1 было использовано 416 Байт памяти и 21 адресов

# В функции func2 было использовано 2530 Байт памяти и 120 адресов

# В функции func3 было использовано 378 Байт памяти и 21 адресов