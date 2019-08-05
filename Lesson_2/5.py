"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def print_sym(start, stop, count=0):
    if start > stop:
        return
    else:
        if count % 10 == 0 and count != 0:
            print('\r')
        print(f'{start:<3}', chr(start), end='  ')
        print_sym(start + 1, stop, count + 1)


def print_sym_1(start, stop):
    for num, cod in enumerate(range(start, stop+1)):
        if num % 10 == 0:
            print('\r')
        print(f'{cod:<3}', chr(cod), end='  ')


# print_sym_1(32, 127)
print_sym(32, 127)

