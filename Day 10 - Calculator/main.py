# In this project, we will be creating a calculator

from art import logo

print(logo)


# Calculations
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
    '/': divide,
}


def calculations():
    num1 = float(input("What is the first number? "))
    for key in operations:
        print(key)

    result = 0
    while True:

        operation_choice = str(input("Pick an operation: "))
        num2 = float(input("What is the next number? "))
        if result != 0:
            num1 = result
        result = operations[operation_choice](num1, num2)
        print(f"{num1} {operation_choice} {num2} = {result}")
        if (str(input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation.: ")) ==
                'n'):
            calculations()


calculations()
