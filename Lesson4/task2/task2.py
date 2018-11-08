import math

def prime_number(n):
    p_num = []
    test_num = 2
    while len(p_num) < n:
        prime = 0
        for i in range(0, len(p_num)):
            if test_num % p_num[i] == 0:
                prime = 1
        if 0 == prime:
            p_num.append(test_num)
        test_num += 1
    return p_num[len(p_num)-1]


def prime_eratos(n):
    num = 0
    size = n * math.log(n) + n * math.log(math.log(n))
    sieve = [1] * round(size)
    sieve[0] = sieve[1] = 0
    for i in range(2, len(sieve)):
        if 1 == sieve[i]:
            for j in range(i+1, len(sieve)):
                if j % i == 0:
                    sieve[j] = 0
    for i in range(2, len(sieve)):
        if 1 == sieve[i]:
            num += 1
        if num == n:
            return i

