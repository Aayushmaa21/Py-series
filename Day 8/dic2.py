#SEARCHING WORD IN DICTIONARY
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for i in words:
    if i in dictionary:
        print(i, "->", dictionary[i])
    else:
        print(i, "is not in dictionary")

