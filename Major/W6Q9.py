#Given a list of numbers, write a Python program to check if the list contains consecutive integers.
def are_consecutive(nums):
    nums_sorted = sorted(nums)
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] != nums_sorted[i-1] + 1:
            return False
    return True

mylist = [1, 2, 3, 4, 5, 7]
result = are_consecutive(mylist)
print(f"The list {mylist} contains consecutive integers: {result}")
