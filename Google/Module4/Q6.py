def count_letters(text):
  # Initialize a new dictionary.
  dictionary = {} 
  
  # Complete the for loop
  for letter in text.lower():
    
    # Check if character is a letter
    if letter.isalpha():
      
      # Check if letter is not already in dictionary
      if letter not in dictionary:
        
           # Add letter as key with initial value 0
           dictionary[letter] = 0  
      
      # Increment the count value
      dictionary[letter] += 1  
      
  return dictionary


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}