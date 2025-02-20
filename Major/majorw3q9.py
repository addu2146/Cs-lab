def swap_values(a, b):
    # Swap the values using addition and subtraction
    a = a + b  # Step 1: a becomes the sum of a and b
    b = a - b  # Step 2: b becomes the original value of a
    a = a - b  # Step 3: a becomes the original value of b
    return a, b

# Test the function
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))

print(f"Before swapping: a = {a}, b = {b}")
a, b = swap_values(a, b)
print(f"After swapping: a = {a}, b = {b}")
