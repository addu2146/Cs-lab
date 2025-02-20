def revWords(mystring):
    revwordstring = ''
    words = mystring.split()
    for word in words:
        revword = ''
        for char in word:
            revword = char + revword
        revwordstring = revwordstring + revword + ' '
    return revwordstring

string = "my name is adnan"
reversed_string = revWords(string)
print(reversed_string)
