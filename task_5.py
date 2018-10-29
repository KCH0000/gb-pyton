a = input('Введите букву латиского алфавита: ').upper()
b = input('Введите еще одну букву латиского алфавита: ').upper()

if a != b:
    aAbcPosition = ord(a) - ord("A") + 1
    bAbcPosition = ord(b) - ord("A") + 1
    count = abs(aAbcPosition - bAbcPosition) - 1
    print(f'Буква {a} {aAbcPosition}-я по счету буква')
    print(f'Буква {b} {bAbcPosition}-я по счету буква')
    print(f'Между буквами {a} и {b} {count} еще букв(a)')
else:
    print('Буквы совпадают')
