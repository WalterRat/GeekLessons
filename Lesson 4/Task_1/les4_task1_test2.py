"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
"""
import timeit
import cProfile


def reverse_2(num):
    res = 0
    while num != 0:
        if num // 10 == 0:
            res = res + (num % 10)
            break
        res = (res + (num % 10)) * 10
        num = num // 10
    return res

print(timeit.timeit('reverse_2(10)', number=1000, globals=globals()))       # 0.00031130000000000047
print(timeit.timeit('reverse_2(100)', number=1000, globals=globals()))      # 0.00046389999999999973
print(timeit.timeit('reverse_2(1000)', number=1000, globals=globals()))     # 0.0005991000000000017
print(timeit.timeit('reverse_2(10000)', number=1000, globals=globals()))    # 0.000816299999999999


cProfile.run('reverse_2(10000)')
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les4_task1_test2.py:8(reverse_2)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0
