"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def count(number, search):
    result = 0
    while number != 0:
        if number % 10 == search:
            result += 1
            number = number // 10
        else:
            number = number // 10
    return f"Кол-во встречающихся значений: {result}"


print(count(int(input("Введите число: ")), int(input("Введите цифру: "))))
