mylist = list(range(1, 100, 1))
evenlist = []
oddlist = []

for num in mylist:
    if num % 2 == 0:
        evenlist.append(num)
    else:
        oddlist.append(num)

print(evenlist)
