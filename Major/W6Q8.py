#Given a list containing characters and numbers, the task is to add only numbers from a list (Use is instance () function).
def sum_numbers(list):
    total = 0
    for item in list:
        if isinstance(item, (int)):
            total += item
    return total

example_list = [1, 'a', 2, 'b', 3, 'c']
result = sum_numbers(example_list)
print(f"The sum of numbers in the list is: {result}")
