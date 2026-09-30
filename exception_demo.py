# This function safely divides two numbers.
def safe_divide(a, b):

    if b == 0:
        raise ValueError("Cannot divide by zero")

    return a / b


# Test normal division.
try:
    result = safe_divide(10, 2)
    print("10 / 2 = " + str(result))

except ValueError as error:
    print("Error: " + str(error))

finally:
    print("Division operation completed")


# Test division by zero.
try:
    result = safe_divide(10, 0)
    print("10 / 0 = " + str(result))

except ValueError as error:
    print("Error: " + str(error))

finally:
    print("Division operation completed")


# Demonstrate catching a generic exception.
try:
    number = int("Python")

except Exception as error:
    print("A general error occurred: " + str(error))