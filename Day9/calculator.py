
from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 -n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("What is the first number?"))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above:")
num2 = int(input("What is the second number?"))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
decision = input("Type 'y' to continue calculation or type 'n' to exit:")

while decision == "y":
    old = answer
    operation_symbol = input("Pick another operation:")
    num3 = int(input("What is the next number?"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(answer, num3)
    print(f"{old} {operation_symbol} {num3} = {answer}")
    decision = input("Type 'y' to continue calculation or type 'n' to exit:")

print("Thank you, bye bye!")