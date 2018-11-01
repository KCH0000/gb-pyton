for i in range(32, 128, 10):
    line = ''
    for j in range(i, i + 10):
        line = line + f' {j} = {chr(j)}'
    print(line)
