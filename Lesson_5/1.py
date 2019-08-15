"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

import collections


def get_avg():
    company = collections.namedtuple('Company', 'Name quarter_I quarter_II quarter_III quarter_IV profit_sum')
    n = int(input('Введите колличество компаний: '))
    profit_all = 0
    companies = []
    for i in range(n):
        name = input('Введите название компании: ')
        profit_1, profit_2, profit_3, profit_4 = \
            list(map(int, input('Введите прибыль за четыре квартала года через пробел: ').split()))
        profit = profit_1 + profit_2 + profit_3 + profit_4
        profit_all += profit
        company_i = company(Name=name,
                            quarter_I=profit_1,
                            quarter_II=profit_2,
                            quarter_III=profit_3,
                            quarter_IV=profit_4,
                            profit_sum=profit)
        companies.append(company_i)
    avg_year = profit_all / n
    return companies, avg_year


def print_company(companies, avg_year):
    more_avg = []
    less_avg = []
    for company in companies:
        if company[5] > avg_year:
            more_avg.append(company[0])
        elif company[5] < avg_year:
            less_avg.append(company[0])
    print(f"Прибыль выше среднего {' '.join(more_avg)}")
    print(f"Прибыль ниже среднего {' '.join(less_avg)}")


def main():
    try:
        companies, avg_year = get_avg()
        print_company(companies, avg_year)
    except ValueError:
        print('Неверный тип данных')


if __name__ == '__main__':
    main()
