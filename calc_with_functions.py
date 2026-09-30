# Function to add two numbers
def add(a, b):
    return a + b


# Function to subtract two numbers
def subtract(a, b):
    return a - b


# Function to multiply two numbers
def multiply(a, b):
    return a * b


# Function to divide two numbers
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# Function to select the correct operation
def calculate(a, b, op):
    if op == "+":
        return add(a, b)
    elif op == "-":
        return subtract(a, b)
    elif op == "*":
        return multiply(a, b)
    elif op == "/":
        return divide(a, b)
    else:
        return "Error: Invalid operation."


# Main program
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")

    result = calculate(num1, num2, operation)

    print("Result: " + str(result))

except ValueError as error:
    print("Error: " + str(error))