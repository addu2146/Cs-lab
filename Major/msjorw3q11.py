import math

def is_perfect_square(x):
    return int(math.sqrt(x))**2 == x

def is_fibonacci_number(n):
    # Check if one of the conditions for being a Fibonacci number is true
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Test the function
number = int(input("Enter a number to check if it is a Fibonacci number: "))
if is_fibonacci_number(number):
    print(f"{number} is a Fibonacci number.")
else:
    print(f"{number} is not a Fibonacci number.")
