"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве. Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения.
"""

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

new = MIN_ITEM
for i in array:
    if i < 0:
        if i > new:
            new = i
    elif i == 0:
        print("В массиве нет отрицательных элементов")
print(new)
