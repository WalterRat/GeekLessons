"""1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком. Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

"""
from random import *

array = [randint(-100, 101) for i in range(10)]

shuffle(array)
print(array)


def bubble(data):
    for n in range(len(data) - 1, 0, -1):
        already_sorted = True
        for i in range(n):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                already_sorted = False
        if already_sorted == True:
            break
    return data


bubble(array)
print(array)
