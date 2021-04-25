"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def sum(number):
    even = 0
    odd = 0
    while number != 0:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        number = number // 10
    return f"Чётных - {even}. Нечётных - {odd}"


print(sum(int(input("Введите число: "))))
