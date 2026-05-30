numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("\nPrevious list contents:", numbers)  # Printing altered list contents.

numbers[1] = numbers[4]  
print("Previous list contents:", numbers)  

print("\nList length:", len(numbers))  # Printing the list's length.
