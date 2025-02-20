#Q5. String Method Tasks:
data = "Python rules!"

# 1. Obtain a list of the words in the string.
words = data.split()
print("Words:", words)

# 2. Convert the string to uppercase.
upper_case = data.upper()
print("Uppercase:", upper_case)

# 3. Locate the position of the string "rules".
position = data.find("rules")
print("Position of 'rules':", position)

# 4. Search a given character ('r').
char_position = data.find('r')
print("Position of 'r':", char_position)

# 5. Replace the exclamation point with a question mark.
replaced = data.replace("!", "?")
print("Replaced string:", replaced)
