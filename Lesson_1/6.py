# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.


num_letter = int(input('Введите номер буквы в алфавите '))
first = ord('a')
print(chr(first + num_letter - 1))

# or
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
print(LETTERS[num_letter - 1])
