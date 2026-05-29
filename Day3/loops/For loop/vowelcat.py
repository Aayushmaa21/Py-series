a = 'Gregory'
a = a.upper()

result = ""

for letter in a:
    if letter in "AEIOU":
        continue
    else:
        result +=letter

print("After removing vowels:", result)