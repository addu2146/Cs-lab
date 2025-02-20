mylist = [1, 3, 4, 23, 2, 43, 54, 6, 7, 8, 56, 4, 3, 2, 43, 1]

largest = float('-inf')
secondlargest = float('-inf')

for num in mylist:
    if num > largest:
        secondlargest = largest
        largest = num
    elif num > secondlargest and num < largest:
        secondlargest = num

print(secondlargest)
