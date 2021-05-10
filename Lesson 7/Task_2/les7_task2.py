"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

from random import *

array = [randint(0, 51) for i in range(10)]

shuffle(array)
print(array)


def merge(left_list, right_list):
    sorted_list = []
    left_index = right_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_index < left_list_length and right_index < right_list_length:
            if left_list[left_index] <= right_list[right_index]:
                sorted_list.append(left_list[left_index])
                left_index += 1
            else:
                sorted_list.append(right_list[right_index])
                right_index += 1

        elif left_index == left_list_length:
            sorted_list.append(right_list[right_index])
            right_index += 1
        elif right_index == right_list_length:
            sorted_list.append(left_list[left_index])
            left_index += 1

    return sorted_list


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2

    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    return merge(left_list, right_list)

print(merge_sort(array))
