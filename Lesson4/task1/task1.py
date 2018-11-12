START = 2
# STOP = 99999
C_START = 2
C_STOP = 9


def multiplicity(num):
    res = [0] * C_STOP
    for i in range(START, num + 1):
        for j in range(C_START, C_STOP + 1):
            if i >= j and i % j == 0:
                res[j - 1] += 1
    return res


def test(func):
    lst = [0, 49999, 33333, 24999, 19999, 16666, 14285, 12499, 11111]
    if lst == func(99999):
        print('Test OK')
    else:
        print('Function panic')


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)