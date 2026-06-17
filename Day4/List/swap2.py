my_list =[5,3,8,1,10]
length = len(my_list)
for i in range(length // 2):
    my_list[i],my_list[length - i-1]=my_list[length - i-1], my_list[i]

print(my_list)