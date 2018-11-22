# Определение количества различных подстрок с использованием хеш-функции. Пусть дана строка S длиной N. Например,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 из модуля hashlib или встроенную функцию hash()


def substring_counter(string):
    str_hashes = set()
    for primary in range(len(string)):
        for secondary in range(primary + 1, len(string) + 1):
            str_hashes.add(hash(string[primary:secondary]))
    return len(str_hashes) - 1  # Вычитаем саму строку


test_string = input("Введите строку для растерзания: ")
print(f'Количество подстрок: {substring_counter(test_string)}')


