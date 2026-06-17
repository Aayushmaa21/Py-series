list_1 = [1]
list_2 = list_1 #linking
list_3 = list_1.copy() #actually copyinh
list_1[0] = 2
print(list_2)
print(list_3)
