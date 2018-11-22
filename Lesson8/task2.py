# Закодируйте любую строку (хотя бы из трех слов) по алгоритму Хаффмана.

from collections import Counter
from collections import deque
import time
import sys
import string
import random


class Node:
    def __init__(self, right, left):
        self.right = right
        self.left = left

    def step(self, symbols_dic, binary_code):
        self.left.step(symbols_dic, binary_code + "0")
        self.right.step(symbols_dic, binary_code + "1")


class Leaf:
    def __init__(self, symbol):
        self.symbol = symbol

    def step(self, symbols_dic, binary_code):
        symbols_dic[self.symbol] = binary_code if len(binary_code) > 0 else '0'

    def __repr__(self):
        return self.symbol


class Huffman:
    def __init__(self, _string):
        self.huffnam_tabel = {}
        self.tree = deque()
        self.string = _string

    def __repr__(self):
            return self.string

    def encode(self):
        if self.huffnam_tabel != {} or self.string == '':
            return self.string
        for symbol, frequency in Counter(self.string).items():
            self.tree.append((frequency, Leaf(symbol)))
        self._sort()

        while len(self.tree) > 1:
            frequency_left, left = self.tree.popleft()
            frequency_right, right = self.tree.popleft()
            self._insert((frequency_left + frequency_right, Node(right, left)))

        root: Node = Node(self.tree[0][1].right, self.tree[0][1].left) if isinstance(self.tree[0][1], Node) \
            else Leaf(self.tree[0][1].symbol)
        root.step(self.huffnam_tabel, "")
        self.tree.clear()
        self.string = "".join(self.huffnam_tabel[c] for c in self.string)
        return self.string

    def decode(self):
        if self.huffnam_tabel == {} or self.string == '':
            return self.string
        decoded = ''
        symbol = ''
        for c in self.string:
            symbol += c
            for key in self.huffnam_tabel:
                if self.huffnam_tabel[key] == symbol:
                    decoded += key
                    symbol = ''
                    break
        self.huffnam_tabel = {}
        self.string = decoded
        return self.string

    def _sort(self):
        n = 0
        while len(self.tree) > n:
            for i in range(len(self.tree) - 1 - n):
                if self.tree[i][0] > self.tree[i + 1][0]:
                    self.tree[i], self.tree[i + 1] = self.tree[i + 1], self.tree[i]
            n += 1

    def _insert(self, obj):
        i = 0
        while i < len(self.tree) and self.tree[i][0] < obj[0]:
            i += 1
        if i < len(self.tree):
            self.tree.insert(i, obj)
        else:
            self.tree.append(obj)


def _joke():
    for _ in range(6):
        print('.', end='')
        sys.stdout.flush()
        time.sleep(0.3)
    return True


s = input('Введите секретное сообщение: ')
s = Huffman(s)

print('Ахалай махалай, сяськи масяськи')
_joke()
s.encode()
print(f'\nКодовое сообещние \n {s}')

print('Раскодируем')
_joke()
s.decode()
print(f'\nИсходное сообщение \n {s}')


def test_huffman(n, _len):
    for _ in range(n):
        test_string = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase +
                                            string.digits) for _ in range(_len))
        code = Huffman(test_string)
        code.encode()
        if test_string != code.decode():
            print(test_string)
            print(code)
            print("Test Fail")
    print("Test OK")

test_huffman(100, 1000)
