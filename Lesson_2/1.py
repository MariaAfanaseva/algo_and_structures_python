"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""


def num_operation():
    try:
        num_1 = int(input('Введите число 1: '))
        num_2 = int(input('Введите число 2: '))
        operation = input('Введите операцию(0 (для отмены), +, -, *, /: ')
        if operation == '0':
            return
        elif operation == '+':
            print(num_1 + num_2)
        elif operation == '-':
            print(num_1 - num_2)
        elif operation == '*':
            print(num_1 * num_2)
        elif operation == '/':
            if num_2 == 0:
                print('На 0 делить нельзя')
            else:
                print(num_1 / num_2)
        else:
            print('Вы ввели неправильную операцию')
        num_operation()
    except ValueError:
        print('Вы ввели не число')
        num_operation()


num_operation()

#  or


def num_operation_1():
    while True:
        try:
            num_1 = int(input('Введите число 1: '))
            num_2 = int(input('Введите число 2: '))
        except ValueError:
            print('Вы ввели не число')
            continue
        operation = input('Введите операцию(0 (для отмены), +, -, *, /: ')
        if operation == '0':
            print('До свидания')
            break
        elif operation == '+':
            print(num_1 + num_2)
        elif operation == '-':
            print(num_1 - num_2)
        elif operation == '*':
            print(num_1 * num_2)
        elif operation == '/':
            if num_2 == 0:
                print('На 0 делить нельзя')
            else:
                print(num_1 / num_2)
        else:
            print('Вы ввели неправильное значение')


num_operation_1()
