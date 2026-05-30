my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
to_find = int(input("Enter number to search: "))

found = 0
for i in range(len(my_list)):
    if  my_list[i] == to_find :
        print("Found at :",i+1)
        found = 1
        break 

if found ==0 :   
    print("Not found!!")
