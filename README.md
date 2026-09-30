# Python Lab 4

## Functions, Tuples, Dictionaries, and Exceptions

This repository contains Python programs demonstrating functions, parameters, return values, tuples, dictionaries, data processing, and exception handling.

## Files

- `basic_functions.py` - Demonstrates functions with parameters, default values, return values, and boolean results.
- `calc_with_functions.py` - A calculator that uses separate functions for arithmetic operations and handles errors using exceptions.
- `tuples_dicts.py` - Demonstrates tuples, tuple immutability, dictionaries, adding entries, and updating values.
- `data_processing.py` - Uses functions, tuples, dictionaries, loops, and exception handling to calculate course grade averages.
- `exception_demo.py` - Demonstrates raising and catching exceptions and using the `finally` block.

## Example Output - basic_functions.py

```text
Hello, Nikhil! Welcome!
Hello! Welcome!
10 + 5 = 15
4 is even: True
7 is even: False
```

## Example Output - calc_with_functions.py

### Normal Calculation

```text
Enter the first number: 7
Enter the second number: 3
Choose an operation (+, -, *, /): *
Result: 21.0
```

### Division by Zero

```text
Enter the first number: 10
Enter the second number: 0
Choose an operation (+, -, *, /): /
Error: Cannot divide by zero.
```

### Invalid Input

```text
Enter the first number: abc
Error: could not convert string to float: 'abc'
```

## Example Output - tuples_dicts.py

```text
First month: January
Last month: December
Tuples are immutable, error: 'tuple' object does not support item assignment

Students and grades:
Alice: 90
Bob: 85
Charlie: 78
David: 88

Updated Bob's grade:
Bob: 92

Updated student list:
Alice: 90
Bob: 92
Charlie: 78
David: 88
```

## Example Output - data_processing.py

```text
The average grade for Math is 88.75
The average grade for Science is 83.5
The average grade for History is 78.75
Warning: No grades are available.
No average available for English.
```

## Example Output - exception_demo.py

```text
10 / 2 = 5.0
Division operation completed
Error: Cannot divide by zero
Division operation completed
A general error occurred: invalid literal for int() with base 10: 'Python'
```

## What I Learned

In this lab, I learned how to create and use functions in Python. I practiced passing parameters to functions and using `return` statements to return values. I also learned how functions can call other functions to make programs more organized and reusable.

I learned that tuples are immutable, which means their values cannot be changed after they are created. I also practiced using dictionaries to store information as key-value pairs and learned how to add and update dictionary entries.

I used functions, tuples, dictionaries, and loops together to process student grade data and calculate averages.

Finally, I learned how to handle errors using `try`, `except`, and `finally`. I also practiced using `raise` to intentionally create an exception when an invalid condition occurs, such as attempting to divide by zero.

Overall, this lab helped me understand how functions, data structures, and exception handling can be combined to create more organized and reliable Python programs.