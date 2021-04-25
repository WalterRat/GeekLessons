"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

array = [0] * 8
num = 2

for i in range(2,100):
    for k in range(2,10):
        if i % k == 0:
            array[k-2] += 1
print(array)

for i in array:
    print(f'{num} - {i}')
    num+=1