#4. Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number:
def create_square_tuples(n):
    return [(i, i**2) for i in range(1, n+1)]

# Example usage
n = 5
print(create_square_tuples(n))
