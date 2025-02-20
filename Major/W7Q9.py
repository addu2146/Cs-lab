list1 = list(range(1,100,1))
list2 = list(range(100,200,1))
mergedlist = [*list1 , *list2]
print(mergedlist)