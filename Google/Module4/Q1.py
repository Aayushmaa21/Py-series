def confirm_length(word):
    lengths=0
    # Complete the condition statement using a string operation. 
    if word !=" ":
        lengths = len(word) # Complete the return statement using a string operation.
        return lengths
    else:
        return 0


print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0