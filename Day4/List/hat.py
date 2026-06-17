hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
a = int(input("Enter number to be replaced :  "))
hat_list[2] = a
del hat_list[4]
print(hat_list)
