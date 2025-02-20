def sum_of_digits(n):
    # Convert the number to a string to easily iterate over digits
    n = abs(n)  # Ensure the number is positive
    digit_sum = sum(int(digit) for digit in str(n))
    return digit_sum

# Example use 
number = 12345
print("Sum of digits:", sum_of_digits(number))
