a = 'Gregory'
a = a.upper()

for letter in a:
    if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        continue
    else:
        print("Removal of vowel: ", letter)