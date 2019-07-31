# 1.	Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.


def get_result():
    number = int(input('Ведите трехзначное число: '))
    if number // 1000 != 0 or number // 100 == 0 or number // 10 == 0:
        print('Вы ввели не трехзначное число')
        quit()
    a = number % 10
    number //= 10
    b = number % 10
    number //= 10
    c = number % 10
    sum_num = a + b + c
    com_num = a * b * c
    print(f'Сумма - {sum_num}')
    print(f'Произведение - {com_num}')


try:
    get_result()
except ValueError:
    print('Вы ввели не число')








