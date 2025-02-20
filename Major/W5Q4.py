def occurences(mystring):
    mystring.lower()
    words=mystring.split()
    WORDS = set(words)
    for word in WORDS:
         print(f"The word {word} occurs { words.count(word)} times")

sentence = "my name is adnan is name my"
occurences(sentence)