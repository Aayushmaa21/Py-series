def string_words(string):
    # Split the string into words and count them
    return len(string.split())


print(string_words("Hello, World"))  # Should print 2
print(string_words("Python is awesome"))  # Should print 3
print(string_words("Keep going"))  # Should print 2
print(string_words("Have a nice day"))  # Should print 4