def multiply_by_7(n):
    # Multiply by 8 (left shift by 3) and then subtract the number
    return (n << 3) - n

# Test the function
number = int(input("Enter a number: "))
result = multiply_by_7(number)
print(f"{number} multiplied by 7 is {result}")
