#2. Find the Union of Two Lists:
def union_of_lists(list1, list2):
    return list(set(list1) | set(list2))


list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print(union_of_lists(list1, list2))
