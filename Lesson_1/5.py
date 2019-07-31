#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.


letter_1 = input('Введите букву ')
letter_2 = input('Введите букву ')
first = ord('a') - 1
place_1 = ord(letter_1) - first
place_2 = ord(letter_2) - first
print(f'Место в алфавите {place_1} и {place_2}')
print(f'Между ними {abs(place_2 - place_1) - 1} букв')

#  or

LETTERS = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
           'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
           'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
           'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

place1 = LETTERS[letter_1]
place2 = LETTERS[letter_2]
print(f'Место в алфавите {place1} и {place2}')
print(f'Между ними {abs(place2 - place1) - 1} букв')

