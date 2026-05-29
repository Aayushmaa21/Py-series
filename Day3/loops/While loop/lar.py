# Store the current largest number here.
largest_number = -4444

number = int(input("Enter a number or type -1 to stop: "))


while number != -1:
    #Is number larger than largest_number?
    if number > largest_number:
        #IF Yes, update largest_number.
        largest_number = number
    number = int(input("Enter a number or type -1 to stop: "))

print("The largest number is:", largest_number)

