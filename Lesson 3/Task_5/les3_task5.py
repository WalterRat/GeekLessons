"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать
"""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max, min = array[0], array[0]
max_index = 0
min_index = 0
sum = 0

for i in range(0, SIZE):
    if array[i] > max:
        max = array[i]
        max_index = i

for i in range(0, SIZE):
    if array[i] < min:
        min = array[i]
        min_index = i

if min_index > max_index:
    array[max_index], array[min_index] = array[min_index], array[max_index]

for i in array[min_index + 1: max_index]:
    sum += i
print(sum)
