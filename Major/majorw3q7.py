
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

print("Before swapping: a = {a}, b = {b}")

# Use XOR to swap the values
a = a ^ b  # Step 1: a now holds the XOR of a and b
b = a ^ b  # Step 2: b now holds the original value of a
a = a ^ b  # Step 3: a now holds the original value of b

# Print the swapped values
print(f"After swapping: a = {a}, b = {b}")
