from collections import deque

first_number = deque(input("Введите первое число: ").upper())
second_number = deque(input("Введите второе число: ").upper())

hex_numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
               'C': 12, 'D': 13, 'E': 14, 'F': 15}
hex_numbers_reverse = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 'A',
                       '11': 'B', '12': 'C', '13': 'D', '14': 'E', '15': 'F', }


def transfer(number):
    for i in range(len(number)):
        number[i] = hex_numbers.get(number[i])


transfer(first_number)
transfer(second_number)


def sixteen_at_ten(number):
    size = len(number) - 1
    result = 0
    for i in range(len(number)):
        result += int(number[i]) * 16 ** (size)
        size -= 1
    number[0] = result


sixteen_at_ten(first_number)
sixteen_at_ten(second_number)

multiplication = first_number[0] * second_number[0]
addition = first_number[0] + second_number[0]


def ten_at_sixteen(number):
    result = deque()
    remains = 16
    whole = 0
    while remains > 15:
        remains, whole = divmod(number, 16)
        number = number // 16
        result.appendleft(hex_numbers_reverse.get(str(whole)))
    result.appendleft(hex_numbers_reverse.get(str(remains)))
    return result


print(f'Произведение чисел - {list(ten_at_sixteen(multiplication))}')
print(f'Сумма чисел - {list(ten_at_sixteen(addition))}')