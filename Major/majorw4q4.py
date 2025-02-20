def factorial(n):
    # Check for non-negative integer
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    # Initialize result
    result = 1
    
    # Loop to calculate the factorial
    for i in range(1, n + 1):
        result *= i
    
    return result

# main part
number = int(input("Enter a non-negative integer: "))
print(f"The factorial of {number} is: {factorial(number)}")
