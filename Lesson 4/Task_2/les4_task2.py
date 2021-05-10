import timeit
import cProfile


def sieve(number): # С помощью алгоритма «Решето Эратосфена»
    array = [i for i in range(number**2)]
    array[1] = False
    for i in range(2, number**2):
        if array[i] != False:
            j = i + i
            while j < number**2:
                array[j] = False
                j += i

    res = [item for item in array if item != False]
    return res[number-1]

print(timeit.timeit('sieve(2)', number=1000, globals=globals()))        # 0.0020271000000000004
print(timeit.timeit('sieve(4)', number=1000, globals=globals()))        # 0.007180800000000001
print(timeit.timeit('sieve(8)', number=1000, globals=globals()))        # 0.0293391
print(timeit.timeit('sieve(16)', number=1000, globals=globals()))       # 0.1323692
print(timeit.timeit('sieve(32)', number=1000, globals=globals()))       # 2.8565587
print(timeit.timeit('sieve(64)', number=1000, globals=globals()))       # 12.2195331

cProfile.run('sieve(500)')
#          6 function calls in 0.240 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.240    0.240 <string>:1(<module>)
#         1    0.006    0.006    0.006    0.006 les4_task2.py:16(<listcomp>)
#         1    0.224    0.224    0.238    0.238 les4_task2.py:6(sieve)
#         1    0.008    0.008    0.008    0.008 les4_task2.py:7(<listcomp>)
#         1    0.000    0.000    0.240    0.240 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0



def prime(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return prime[-1]

print(timeit.timeit('prime(2)', number=1000, globals=globals()))            # 0.0004037999999999542
print(timeit.timeit('prime(4)', number=1000, globals=globals()))            # 0.0009405000000000108
print(timeit.timeit('prime(8)', number=1000, globals=globals()))            # 0.002836600000000189
print(timeit.timeit('prime(16)', number=1000, globals=globals()))           # 0.009705799999999876
print(timeit.timeit('prime(32)', number=1000, globals=globals()))           # 0.032155500000000004
print(timeit.timeit('prime(64)', number=1000, globals=globals()))           # 0.1134056000000001
print(timeit.timeit('prime(128)', number=1000, globals=globals()))          # 0.4102232999999993
print(timeit.timeit('prime(256)', number=1000, globals=globals()))          # 1.6249247000000002
print(timeit.timeit('prime(512)', number=1000, globals=globals()))          # 6.704026799999999
print(timeit.timeit('prime(1024)', number=1000, globals=globals()))         # 27.3558923

cProfile.run('prime(2000)')
#         2003 function calls in 0.122 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.122    0.122 <string>:1(<module>)
#         1    0.122    0.122    0.122    0.122 les4_task2.py:43(prime)
#         1    0.000    0.000    0.122    0.122 {built-in method builtins.exec}
#      1999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
#
#
# Process finished with exit code 0
#
