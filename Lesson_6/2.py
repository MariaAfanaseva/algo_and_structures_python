"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
from pympler import asizeof


class OperationsNum:
    def __init__(self, num_1, num_2):
        self.num_first = num_1
        self.num_second = num_2

    def __add__(self, other):
        return list(hex(int(self.num_first, 16) + int(self.num_second, 16)).upper())[2:]

    def __mul__(self, other):
        return list(hex(int(self.num_first, 16) * int(self.num_second, 16)).upper())[2:]


class OperationsNumSlot:
    __slots__ = ('num_first', 'num_second')

    def __init__(self, num_1, num_2):
        self.num_first = num_1
        self.num_second = num_2

    def __add__(self, other):
        return list(hex(int(self.num_first, 16) + int(self.num_second, 16)).upper())[2:]

    def __mul__(self, other):
        return list(hex(int(self.num_first, 16) * int(self.num_second, 16)).upper())[2:]


def main():
    try:
        num_1, num_2 = input('Введите два числа в шестнадцатеричном формате через пробел: ').split()
        result = OperationsNum(num_1, num_2)
        result_1 = OperationsNumSlot(num_1, num_2)
        print(result.__dict__)
        print(asizeof.asizeof(result))
        result.count = 0
        print(result.__dict__)
        print(asizeof.asizeof(result))

        print(result_1.__slots__)
        print(asizeof.asizeof(result_1))
        # print(f'Сумма чисел {result + result}, поизведение {result * result}')
    except ValueError:
        print('Неверный формат')


if __name__ == '__main__':
    main()


"""
Класс со __slots__ занимает в два раза меньше памяти 
{'num_first': 'Ф2', 'num_second': 'С4А'}
456
('num_first', 'num_second')
216
"""
