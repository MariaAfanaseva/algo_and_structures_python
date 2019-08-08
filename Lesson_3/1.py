# 1.	В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

lst = [i for i in range(2, 100)]
# print(lst)
for num in range(2, 10):
    count = 0
    for i in lst:
        if i % num == 0:
            count += 1
    print(f'В диапазоне от 2 до 99 кратны {num} чисел {count}')
