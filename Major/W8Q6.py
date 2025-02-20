#6. Count the Number of Characters (Character Frequency) in a String:
from collections import Counter

def count_char_frequency(s):
    return dict(Counter(s))

# Example usage
string = "hello"
print(count_char_frequency(string))
