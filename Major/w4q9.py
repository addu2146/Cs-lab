def count_letters(s):
    uppercase_count = 0
    lowercase_count = 0

    for char in s:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return uppercase_count, lowercase_count

string = "Hello, World! It's a beautiful day."
uppercase_count, lowercase_count = count_letters(string)

print(f"Number of uppercase letters: {uppercase_count}")
print(f"Number of lowercase letters: {lowercase_count}")
