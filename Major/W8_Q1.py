#1. Sort a List According to the Length of the Elements:
def sort_by_length(lst):
    return sorted(lst, key=len)
lst = ["apple", "banana", "kiwi", "cherry", "fig"]
print(sort_by_length(lst))
