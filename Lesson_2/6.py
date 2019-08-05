"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
import random


def guess(number, num_try=1):
    try:
        if num_try == 11:
            print('Вы проиграли')
            return
        else:
            n = int(input(f'Введите число. Попытка номер {num_try} из 10: '))
            if n == number:
                print('Вы угадали!')
                return
            elif n > number:
                print('Загаданное число меньше')
            else:
                print('Загаданное число больше')
            guess(number, num_try + 1)
    except ValueError:
        print('Вы ввели не число')
        guess(number, num_try)


def main():
    number = random.randint(1, 100)
    # print(number)
    print('Число загадано, отгадайте!')
    guess(number)


if __name__ == '__main__':
    main()
