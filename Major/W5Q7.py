def reverse_string(s):
    reversed_s = ''
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s


original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print(reversed_string) 
