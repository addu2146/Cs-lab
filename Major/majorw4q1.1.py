def average_of_five_numbers(num1, num2, num3, num4, num5):
    
    total = num1 + num2 + num3 + num4 + num5
    
    average = total / 5
    return average


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))
num5 = float(input("Enter the fifth number: "))

result = average_of_five_numbers(num1, num2, num3, num4, num5)
print(f"The average of the five numbers is: {result}")
