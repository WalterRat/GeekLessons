# Python 3.8
# OC - 64 bit

"""Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)."""

from count_memory import count_memory

num1 = int(input("Введите 1е число: "))  # 100
num2 = int(input("Введите 2е число: "))  # 200
num3 = int(input("Введите 3е число: "))  # 300
# num 1
if (num2 < num1 < num3) or (num3 < num1 < num2):
    print(num1)
# num 2
if (num1 < num2 < num3) or (num3 < num2 < num1):
    print(num2)
# num 3
if (num1 < num3 < num2) or (num2 < num3 < num1):
    print(num3)

sum_ = 0
var_lst = (num1, num2, num3)
for i in var_lst:
    sum_ += count_memory(i)
print(f'Под переменные уходит {sum_} байт памяти')
# 200
# Под переменные уходит 42 байт памяти
