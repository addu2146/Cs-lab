x, y, z = 10, 20, 30
smallest = x if (x < y and x < z) else (y if y < z else z)
print("The greatest number is:", smallest)