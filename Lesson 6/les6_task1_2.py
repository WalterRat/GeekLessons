# Python 3.8
# OC - 64 bit

"""Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)."""

from count_memory import count_memory

array = []
for i in range(3):
    array.append(int(input(f"Введите {i + 1} число: ")))  # 100, 200,300
del array[array.index(max(array))], array[array.index(min(array))]
print(array[0])

sum_ = 0
var_lst = (array)
for i in var_lst:
    sum_ += count_memory(i)
print(f'Под переменные уходит {sum_} байт памяти')

# 200
# Под переменные уходит 14 байт памяти

"""
Все варианты программы одинаково занимают 42 байта. 
Просто во 2й программе python выделяет 42 байта на массив из 3х элементов, но потом мы удаляем два элемента из него. 
Поэтому итоговый ответ 2й версии программы вышел 14 байт.
"""