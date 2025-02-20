
def calculate_area(base, height):
    return 0.5 * base * height

def determine_triangle_type(base, height, area):
    if base == height:
        return "Isosceles Triangle"
    elif base != height:
        return "Scalene Triangle"
    elif base == height == (2 * area / base):
        return "Equilateral Triangle"
    else:
        return "Unknown Triangle Type"

base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))

area = calculate_area(base, height)
triangle_type = determine_triangle_type(base, height, area)

print(f"The area of the triangle is {area}")
print(f"The triangle is a {triangle_type}")


