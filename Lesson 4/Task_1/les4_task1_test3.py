"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
"""
import timeit
import cProfile

def reverse_3(num):
    num = str(num)
    return num[::-1]


print(timeit.timeit('reverse_3(10)', number=1000, globals=globals()))       # 0.00033059999999999687
print(timeit.timeit('reverse_3(100)', number=1000, globals=globals()))      # 0.00032180000000000056
print(timeit.timeit('reverse_3(1000)', number=1000, globals=globals()))     # 0.00033019999999999924
print(timeit.timeit('reverse_3(10000)', number=1000, globals=globals()))    # 0.0003245999999999978


cProfile.run('reverse_3(10000)')
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 les4_task1_test3.py:7(reverse_3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0
"""
ВЫВОД: Третий вариант программы(reverse_3()) работает лучше всех, так как срез не тратит много времени на вычисления и прочее. Поэтому для любого значения num время будет примерно одинаково
"""
