my_list= [2,7,4,90,50]

largest = my_list[0]
for i in range(1,len(my_list)):
    if my_list[i] > largest:
        largest = my_list[i]

print("Largest number is : ", largest) 
