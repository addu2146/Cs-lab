import math

def area_of_circle():
    # Accept radius from the user
    radius = float(input("Enter the radius of the circle: "))
    # Calculate the area using the formula A = pi * r**2
    area = math.pi * radius ** 2
    return area

result = area_of_circle()
print(f"The area of the circle is: {result}")
