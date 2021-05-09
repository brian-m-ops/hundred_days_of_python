def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

finished = False

while not finished:
    num1 = int(input("What's the first number?: "))
    num2 = int(input("What's the second number?: "))

    for operator in operations:
        print(operator)

    operation_symbol = input("Pick an operation from the line above: ")
    calc_function = operations[operation_symbol]
    answer = calc_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")
    keep_going = input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.:  ")

    if keep_going == 'n':
        finished = True
