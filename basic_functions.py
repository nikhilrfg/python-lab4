# This function greets the user.
# The default value allows the function to be called without a name.
def greet_user(name=""):
    if name:
        print("Hello, " + name + "! Welcome!")
    else:
        print("Hello! Welcome!")


# This function takes two numbers and returns their sum.
def add_two_numbers(a, b):
    return a + b


# This function returns True if the number is even.
def is_even(num):
    return num % 2 == 0


# Call greet_user with a name.
greet_user("Nikhil")

# Call greet_user without a name.
greet_user()

# Add two numbers and store the returned value.
sum_result = add_two_numbers(10, 5)
print("10 + 5 = " + str(sum_result))

# Check an even number.
print("4 is even: " + str(is_even(4)))

# Check an odd number.
print("7 is even: " + str(is_even(7)))