"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""
while True:
    print("--------------")
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    choice = input("Выберите операцию '0', '+', '-', '*', '/': ")
    try:
        if choice == "0":
            break
        elif choice == "+":
            result = num1 + num2
        elif choice == "-":
            result = num1 - num2
        elif choice == "*":
            result = num1 * num2
        elif choice == "/":
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("На ноль делить нельзя!")
                continue
        print(f"Ответ: {result}")
    except NameError:
        print("Данной операции не существует")
