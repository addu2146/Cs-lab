import math


def check_prime_or_factor(n):
    if n <= 1:
        return f"{n} is not prime."

    # Check for factors from 2 to sqrt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return f"{n} is not prime. The first factor is {i}."
    
    # If no factors found, it's prime
    return f"{n} is prime."

# Read an integer from the user
num = int(input("Enter an integer: "))

# Call the function and print the result
result = check_prime_or_factor(num)
print(result)
