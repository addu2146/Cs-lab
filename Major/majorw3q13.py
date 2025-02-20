
def gcd(a, b):
    while b != 0:
        a, b = b, a % b  
    return a

# Read two integers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the GCD
result = gcd(num1, num2)

# Output the result
print(f"The GCD of {num1} and {num2} is: {result}")
