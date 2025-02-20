def count_vowels(mystring):
    mystring.lower()
    vowels = "aeiou"
    vowel_count = {v: 0 for v in vowels}
    for character in mystring:
        if character in vowels:
            vowel_count[character] += 1
    return vowel_count

string = "my name is adnan"
vowel_count = count_vowels(string)
for vowel, count in vowel_count.items():
    print(f"{vowel}: {count}")

