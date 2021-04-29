"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
"""
import timeit
import cProfile


def reverse_1(num):
    if num < 10:
        return num
    return str(num % 10) + str(reverse_1(num // 10))


print(timeit.timeit('reverse_1(10)', number=1000, globals=globals()))       # 0.0006073999999999975
print(timeit.timeit('reverse_1(100)', number=1000, globals=globals()))      # 0.0010472000000000016
print(timeit.timeit('reverse_1(1000)', number=1000, globals=globals()))     # 0.0014932
print(timeit.timeit('reverse_1(10000)', number=1000, globals=globals()))    # 0.0020618000000000025


cProfile.run('reverse_1(10000)')
#          8 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#       5/1    0.000    0.000    0.000    0.000 les4_task1_test1.py:8(reverse_1)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0
