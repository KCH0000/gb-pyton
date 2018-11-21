import random
a = 0
a = float(a)
i = 0
max_ = 0

while a != 50:
    a = random.uniform(max_ - 0.000000000001, 50)
    if max_ < a:
        max_ = a
        print(i, max_)
    i += 1
else:
    print(i, max_)