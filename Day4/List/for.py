my_list = [10, 1, 8, 3, 5]
total = 0
 
# for i in my_list:
#     total += i
 
# print(total)

for i in range(len(my_list)): #range(5)
    total += my_list[i]

print(total)
total = 0
for i in my_list:
    total += i
 
print(total)