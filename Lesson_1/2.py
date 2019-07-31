# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 7
b = 9
print(bin(a), int(bin(a), 2))
print(bin(b), int(bin(b), 2))
print(bin(~b), ~b)  # ~n = -(n + 1) двоичная инверсия

a_and_b = a & b
print(bin(a_and_b), a_and_b)  # побитовые и
a_or_b = a | b   # побитовые или
print(bin(a_or_b), a_or_b)

not_or_a_b = a ^ b
print(bin(not_or_a_b), not_or_a_b)  # исключающее или

c = 5
d = 6
print(bin(c), bin(c << 2), c << 2)  # побитовый сдвиг
print(bin(d), bin(d >> 2), d >> 2)
