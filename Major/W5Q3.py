def remove_odd_characters(mystring):
    return mystring[::2]


string = "hippopotamus"
result = remove_odd_characters(string)
print(f"removed characters are : {result}")  
print(f"The string remaining is {string[1::2]}")
