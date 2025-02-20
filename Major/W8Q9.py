#9. Reverse the Words in a String (Palindrome check as well):
def reverse_words(s):
    words = s.split()
    return ' '.join(reversed(words))

def is_palindrome(s):
    return s == s[::-1]

user_input = input("Enter a string: ")
print("Reversed words:", reverse_words(user_input))

if is_palindrome(user_input):
    print(f"The string '{user_input}' is a palindrome!")
else:
    print(f"The string '{user_input}' is not a palindrome!")
