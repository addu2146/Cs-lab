import math

def volume_of_sphere(radius):
    # Volume formula: V = (4/3) * π * r^3
    volume = (4/3) * math.pi * radius**3
    return volume


radius = float(input("enter radius of circle :"))
volume = volume_of_sphere(radius)
print(f"The volume of a sphere with radius {radius} is: {volume}")
