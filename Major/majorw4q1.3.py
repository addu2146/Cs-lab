def perimeter_of_rectangle(length, width):
    # Calculate the perimeter using the formula
    perimeter = 2 * (length + width)
    return perimeter


length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = perimeter_of_rectangle(length, width)
print(f"The perimeter of the rectangle is: {perimeter}")
