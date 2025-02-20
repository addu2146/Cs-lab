def celsius_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using the formula
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


celsius = float(input("Enter the temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}° Celsius is equal to {fahrenheit}° Fahrenheit.")
