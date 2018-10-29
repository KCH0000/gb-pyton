absPosition = int(input('Введите порядковый номер буквы в латинском алфавите '))
if 0 < absPosition < 27:
    a = chr(absPosition + ord('A') - 1)
    print(f'Буква с позицией {absPosition} - {a}')
else:
    print('В алфавите 26 букв')