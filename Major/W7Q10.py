def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def find_second_largest(arr):
    bubble_sort(arr)
    #remove repetition
    distinctarr = list(set(arr))
    distinctarr.sort()
    return distinctarr[-2] if len(distinctarr) >= 2 else None

mylist = [1, 3, 4, 23, 2, 43, 54, 6, 7, 8, 56, 4, 3, 2, 43, 1]
second_largest = find_second_largest(mylist)
print(second_largest)
