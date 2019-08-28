"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""


def counting_frequency_letters(string):
    letters = {}
    for letter in string:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    return letters


def huffman_coding(letters):
    frequency = list(letters.items())
    for letter in letters:
        letters[letter] = ''

    while len(frequency) != 1:
        # print(frequency)
        min1 = min(frequency, key=lambda x: x[1])
        for i in min1[0]:
            letters[i] = '0{0}'.format(letters[i])
        frequency.pop(frequency.index(min1))

        min2 = min(frequency, key=lambda x: x[1])
        for i in min2[0]:
            letters[i] = '1{0}'.format(letters[i])
        frequency.pop((frequency.index(min2)))
        frequency.append((min1[0] + min2[0], min1[1] + min2[1]))
        # print(min1, min2)
        # print(frequency)
        # print(letters)
    return letters


def result_print():
    string = input('Введите строку: ')
    letters = huffman_coding(counting_frequency_letters(string))
    if len(letters) == 1:
        letters[string[0]] = '0'
    for let, cod in letters.items():
        print(let + ': ' + cod)
    for let in string:
        print(letters[let], end='')


result_print()
