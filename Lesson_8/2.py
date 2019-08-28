"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

string = input("Введите строку из маленьких латинских букв: ")
substrings = set()

length = len(string)
for i in range(length):
    for j in range(i, length):
        if i > 0 or i == j:
            print(string[i:j+1])
            substrings.add(hashlib.sha1(string[i:j+1].encode('utf-8')).hexdigest())
        else:
            print(string[i:j])
            substrings.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())

print(substrings)
print(f"Количество различных подстрок в строке '{string}' равно {len(substrings)}")
